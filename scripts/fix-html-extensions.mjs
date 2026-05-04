// Post-build fix: Quartz strips `.html` from static HTML files in content/.
// This script:
//  1. Renames extension-less HTML files in public/ back to *.html
//  2. Patches href="..." in all rendered .html pages so links resolve correctly
//
// Why: Quartz's slugifyFilePath treats .html as a "page extension" and strips
// it, but GitHub Pages serves extension-less files as application/octet-stream,
// which forces browsers to download instead of render.

import { readdir, readFile, writeFile, rename, stat } from "node:fs/promises"
import { join, basename } from "node:path"

const PUBLIC_DIR = "public"
const HTML_SIGNATURES = ["<!doctype", "<html"]

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true })
  const out = []
  for (const e of entries) {
    const full = join(dir, e.name)
    if (e.isDirectory()) out.push(...(await walk(full)))
    else if (e.isFile()) out.push(full)
  }
  return out
}

async function looksLikeHtml(path) {
  try {
    const buf = await readFile(path, "utf-8")
    const head = buf.slice(0, 200).trim().toLowerCase()
    return HTML_SIGNATURES.some((s) => head.startsWith(s))
  } catch {
    return false
  }
}

async function main() {
  const allFiles = await walk(PUBLIC_DIR)
  const extensionless = allFiles.filter((f) => !basename(f).includes("."))

  const renamed = []
  for (const f of extensionless) {
    if (await looksLikeHtml(f)) {
      const newPath = f + ".html"
      await rename(f, newPath)
      renamed.push({
        oldBase: basename(f),
        newBase: basename(f) + ".html",
      })
      console.log(`renamed → ${newPath}`)
    }
  }

  if (renamed.length === 0) {
    console.log("No extension-less HTML files found.")
    return
  }

  // Patch links inside all rendered .html pages.
  const htmlPages = allFiles
    .map((p) => (p.endsWith(".html") ? p : p + ".html"))
    .filter((p, i, arr) => arr.indexOf(p) === i)
    .filter((p) => p.endsWith(".html"))

  let patchedCount = 0
  for (const page of htmlPages) {
    let content
    try {
      content = await readFile(page, "utf-8")
    } catch {
      continue
    }
    let modified = false
    for (const { oldBase, newBase } of renamed) {
      // Match href="...<oldBase>" but only when followed by " or # or ? (URL boundary)
      // and not already followed by .html
      const r1 = new RegExp(`(href|src)="([^"]*?)\\/${oldBase}(?=["#?])`, "g")
      const next1 = content.replace(r1, `$1="$2/${newBase}`)
      if (next1 !== content) {
        modified = true
        content = next1
      }
      const r2 = new RegExp(`(href|src)="${oldBase}(?=["#?])`, "g")
      const next2 = content.replace(r2, `$1="${newBase}`)
      if (next2 !== content) {
        modified = true
        content = next2
      }
    }
    if (modified) {
      await writeFile(page, content)
      patchedCount++
    }
  }

  console.log(
    `\nDone. Renamed ${renamed.length} file(s), patched links in ${patchedCount} page(s).`,
  )
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})
