

$outputDir = "$PSScriptRoot\output"
if (!(Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$outputFile = "$outputDir\ram.json"

$mem = Get-CimInstance Win32_OperatingSystem

$total = [math]::Round($mem.TotalVisibleMemorySize / 1024, 2)   # MB
$free  = [math]::Round($mem.FreePhysicalMemory / 1024, 2)       # MB
$used  = [math]::Round($total - $free, 2)

$percentUsed = [math]::Round(($used / $total) * 100, 2)

$data = @{
    timestamp = (Get-Date).ToString("o")
    ram = @{
        total_mb = $total
        used_mb = $used
        free_mb = $free
        usage_percent = $percentUsed
    }
}

$json = $data | ConvertTo-Json -Depth 5

Set-Content -Path $outputFile -Value $json

Write-Output "[RAM] $percentUsed% -> $outputFile"
