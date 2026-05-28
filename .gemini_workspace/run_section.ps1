param(
  [int]$Section,
  [string]$StartTime,
  [string]$EndTime
)
$env:GEMINI_API_KEY = "AIzaSyAxlaTIDIaYQO6LE1MjSFvGeu0rRMY_hbs"
$env:GEMINI_PRO_MODEL = "gemini-3.1-pro-preview"
Remove-Item Env:UNDICI_PROXY -ErrorAction SilentlyContinue

$q = @"
For this section, capture in DETAIL:
1. EVERY FORMULA written on screen OR spoken aloud — with [mm:ss] timestamp
2. EVERY FORMULA DERIVATION — full step-by-step chain, NOT just the final result. Capture all intermediate steps.
3. EVERY MIND MAP / GRAPH / DIAGRAM / SLIDE on screen — describe axis labels, curve shapes, labeled nodes, exact text on slides, hierarchical structure
4. EVERY KEY CONCEPT the speaker emphasizes — with timestamp and direct quote where memorable
5. Any audience poll questions/results with the exact wording
Do not compress derivations. Preserve all timestamps. Format as Markdown.
"@

$outFile = "E:/Obsedian/Vault/.gemini_workspace/sec$Section.md"
Write-Host "[runner] Section $Section ($StartTime - $EndTime) -> $outFile"
node "E:/Obsedian/Vault/.gemini_workspace/gemini-call.cjs" --out $outFile youtube "https://www.youtube.com/watch?v=IAEASE5GjdI" $q $StartTime $EndTime
Write-Host "[runner] Section $Section exit: $LASTEXITCODE"
