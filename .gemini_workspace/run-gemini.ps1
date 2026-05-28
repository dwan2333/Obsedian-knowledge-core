# Wrapper that sets the same env vars the MCP config uses, then calls gemini-call.cjs.
# Usage: powershell -File run-gemini.ps1 youtube <url> <question> [startTime] [endTime]
param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Args)

$env:GEMINI_API_KEY        = "AIzaSyAxlaTIDIaYQO6LE1MjSFvGeu0rRMY_hbs"
$env:GEMINI_PRO_MODEL      = "gemini-3-pro-preview"
$env:GEMINI_FLASH_MODEL    = "gemini-3-flash-preview"
$env:GEMINI_IMAGE_MODEL    = "gemini-3-pro-image-preview"
$env:UNDICI_PROXY          = "http://127.0.0.1:7897"
$env:NODE_PATH             = "C:/Users/dwan0/AppData/Roaming/npm/node_modules"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$caller = Join-Path $scriptDir "gemini-call.cjs"

# Run node with output captured by PowerShell (stderr goes to host, stdout returned)
& node $caller @Args
