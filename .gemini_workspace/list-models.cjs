#!/usr/bin/env node
const path = require('path');
const MODULES_ROOT = 'C:/Users/dwan0/AppData/Roaming/npm/node_modules';
const GEMINI_MCP_DEPS = path.join(MODULES_ROOT, '@rlabs-inc/gemini-mcp/node_modules');

if (process.env.UNDICI_PROXY) {
  try { require(path.join(MODULES_ROOT, 'gemini-proxy-preload.js')); } catch (e) {}
}

const { GoogleGenAI } = require(path.join(GEMINI_MCP_DEPS, '@google/genai'));
const genAI = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

(async () => {
  try {
    const result = await genAI.models.list();
    for await (const model of result) {
      if (model.name && model.name.includes('gemini') &&
          model.supportedActions && model.supportedActions.includes('generateContent')) {
        console.log(`${model.name}  [in: ${model.inputTokenLimit}, out: ${model.outputTokenLimit}]`);
      }
    }
  } catch (e) {
    console.error('ERROR:', e.message);
    process.exit(1);
  }
})();
