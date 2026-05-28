param([int[]]$Sections = @(3,4,5,6,7,8,9,10))

$plan = @{}
$plan[3]  = '12:00','18:00'
$plan[4]  = '18:00','24:00'
$plan[5]  = '24:00','30:00'
$plan[6]  = '30:00','36:00'
$plan[7]  = '36:00','42:00'
$plan[8]  = '42:00','48:00'
$plan[9]  = '48:00','55:00'
$plan[10] = '55:00','1:03:07'

foreach ($s in $Sections) {
  $st = $plan[$s][0]
  $en = $plan[$s][1]
  Write-Host "=== Section $s ($st - $en) ==="
  & "E:/Obsedian/Vault/.gemini_workspace/run_section.ps1" -Section $s -StartTime $st -EndTime $en
  if ($LASTEXITCODE -ne 0) {
    Write-Host "[batch] Section $s FAILED (exit $LASTEXITCODE) - stopping"
    exit 1
  }
}
Write-Host "[batch] done"
