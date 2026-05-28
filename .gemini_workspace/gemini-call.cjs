#!/usr/bin/env node
/**
 * Direct Gemini caller — bypasses MCP layer.
 * Used by Path C of vault-note-creator skill when MCP tool catalog doesn't expose gemini tools.
 *
 * Usage:
 *   node gemini-call.cjs youtube  <url> <question> [startTime] [endTime]
 *   node gemini-call.cjs url      <url> <question>
 *   node gemini-call.cjs image    <imagePath> <question>
 *   node gemini-call.cjs text     <question>
 *
 * Env vars (read from process.env, set by caller):
 *   GEMINI_API_KEY       (required)
 *   GEMINI_PRO_MODEL     (default: gemini-3-pro-preview)
 *   UNDICI_PROXY         (optional)
 *
 * Outputs: model response text to stdout. Logs to stderr.
 */

const path = require('path');
const fs = require('fs');

const MODULES_ROOT = 'C:/Users/dwan0/AppData/Roaming/npm/node_modules';
const GEMINI_MCP_DEPS = path.join(MODULES_ROOT, '@rlabs-inc/gemini-mcp/node_modules');

// Apply proxy preload if env var set
if (process.env.UNDICI_PROXY) {
  try {
    require(path.join(MODULES_ROOT, 'gemini-proxy-preload.js'));
    process.stderr.write(`[proxy] preload applied: ${process.env.UNDICI_PROXY}\n`);
  } catch (e) {
    process.stderr.write(`[proxy] preload skipped: ${e.message}\n`);
  }
}

const { GoogleGenAI } = require(path.join(GEMINI_MCP_DEPS, '@google/genai'));

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  process.stderr.write('ERROR: GEMINI_API_KEY not set\n');
  process.exit(1);
}

const model = process.env.GEMINI_PRO_MODEL || 'gemini-3-pro-preview';
const genAI = new GoogleGenAI({ apiKey });

function parseTimeToSeconds(time) {
  if (time.includes(':')) {
    const [mins, secs] = time.split(':').map(Number);
    return `${mins * 60 + secs}s`;
  }
  const minMatch = time.match(/(\d+)m/);
  const secMatch = time.match(/(\d+)s/);
  const mins = minMatch ? parseInt(minMatch[1]) : 0;
  const secs = secMatch ? parseInt(secMatch[1]) : 0;
  if (mins > 0 || secMatch) return `${mins * 60 + secs}s`;
  const num = parseInt(time);
  if (!isNaN(num)) return `${num}s`;
  return time;
}

async function withRetry(fn, label, maxAttempts = 5) {
  let lastErr;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastErr = err;
      const cause = err.cause ? (err.cause.code || err.cause.message) : '';
      const msg = err.message || String(err);
      const is503 = msg.includes('"code":503') || msg.includes('UNAVAILABLE');
      const isSocket = cause === 'UND_ERR_SOCKET' || msg.includes('other side closed') || msg.includes('fetch failed');
      const shouldRetry = is503 || isSocket;
      if (!shouldRetry || attempt === maxAttempts) throw err;
      const backoff = is503 ? 30 : 5 * attempt;
      process.stderr.write(`[retry ${attempt}/${maxAttempts}] ${label} failed (${is503 ? '503' : 'socket'}), backoff ${backoff}s\n`);
      await new Promise((r) => setTimeout(r, backoff * 1000));
    }
  }
  throw lastErr;
}

async function callYouTube(url, question, startTime, endTime) {
  const videoPart = {
    fileData: { fileUri: url, mimeType: 'video/*' },
  };
  if (startTime || endTime) {
    const md = {};
    if (startTime) md.startOffset = parseTimeToSeconds(startTime);
    if (endTime) md.endOffset = parseTimeToSeconds(endTime);
    videoPart.videoMetadata = md;
  }
  const contents = [{ role: 'user', parts: [videoPart, { text: question }] }];
  process.stderr.write(`[gemini] model=${model} youtube_call start=${startTime || 'none'} end=${endTime || 'none'}\n`);
  const t0 = Date.now();
  const response = await withRetry(
    () => genAI.models.generateContent({ model, contents }),
    `youtube[${startTime || 'start'}-${endTime || 'end'}]`,
  );
  process.stderr.write(`[gemini] response in ${((Date.now() - t0) / 1000).toFixed(1)}s\n`);
  return response.text || '';
}

async function callUrl(url, question) {
  const contents = [{
    role: 'user',
    parts: [
      { fileData: { fileUri: url, mimeType: 'text/html' } },
      { text: question },
    ],
  }];
  process.stderr.write(`[gemini] url_call model=${model}\n`);
  const response = await genAI.models.generateContent({ model, contents });
  return response.text || '';
}

async function callImage(imagePath, question) {
  const data = fs.readFileSync(imagePath);
  const ext = path.extname(imagePath).slice(1).toLowerCase();
  const mimeMap = { png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', webp: 'image/webp' };
  const mime = mimeMap[ext] || 'image/png';
  const contents = [{
    role: 'user',
    parts: [
      { inlineData: { mimeType: mime, data: data.toString('base64') } },
      { text: question },
    ],
  }];
  process.stderr.write(`[gemini] image_call model=${model} mime=${mime} bytes=${data.length}\n`);
  const response = await genAI.models.generateContent({ model, contents });
  return response.text || '';
}

async function callText(question) {
  process.stderr.write(`[gemini] text_call model=${model}\n`);
  const response = await genAI.models.generateContent({
    model,
    contents: [{ role: 'user', parts: [{ text: question }] }],
  });
  return response.text || '';
}

async function main() {
  // Optional --out <file> writes UTF-8 text to the file instead of stdout.
  const argv = process.argv.slice(2);
  let outFile = null;
  const outIdx = argv.indexOf('--out');
  if (outIdx >= 0) {
    outFile = argv[outIdx + 1];
    argv.splice(outIdx, 2);
  }
  const [subcmd, ...args] = argv;
  try {
    let text;
    if (subcmd === 'youtube') {
      const [url, question, startTime, endTime] = args;
      text = await callYouTube(url, question, startTime, endTime);
    } else if (subcmd === 'url') {
      const [url, question] = args;
      text = await callUrl(url, question);
    } else if (subcmd === 'image') {
      const [imagePath, question] = args;
      text = await callImage(imagePath, question);
    } else if (subcmd === 'text') {
      const [question] = args;
      text = await callText(question);
    } else {
      process.stderr.write(`Unknown subcommand: ${subcmd}\n`);
      process.exit(1);
    }
    if (outFile) {
      fs.writeFileSync(outFile, text, { encoding: 'utf8' });
      process.stderr.write(`[gemini] wrote ${text.length} chars to ${outFile}\n`);
    } else {
      process.stdout.write(text);
    }
  } catch (err) {
    process.stderr.write(`ERROR: ${err.message || err}\n`);
    if (err.cause) {
      process.stderr.write(`CAUSE: ${err.cause.message || JSON.stringify(err.cause)}\n`);
      if (err.cause.code) process.stderr.write(`CAUSE_CODE: ${err.cause.code}\n`);
    }
    if (err.stack) process.stderr.write(err.stack + '\n');
    process.exit(2);
  }
}

main();
