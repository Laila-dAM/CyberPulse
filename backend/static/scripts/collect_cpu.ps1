# scripts/collect_cpu.ps1
# CyberPulse - Collect CPU usage on Windows and save JSON to scripts/output/cpu.json

# create output folder if not exists
$OutDir = Join-Path -Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'output'
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

# collect hostname and timestamp
$hostname = $env:COMPUTERNAME
$timestamp = (Get-Date).ToString("o")

# collect CPU usage (average LoadPercentage)
$cpuObj = Get-CimInstance Win32_Processor | Select-Object -ExpandProperty LoadPercentage
if ($cpuObj -is [array]) { $cpu = [int]([Math]::Round(($cpuObj | Measure-Object -Average).Average)) } else { $cpu = [int]$cpuObj }

# build JSON
$data = [PSCustomObject]@{
    host      = $hostname
    timestamp = $timestamp
    cpu_usage = $cpu
}

$json = $data | ConvertTo-Json -Depth 3

# write to file
$outFile = Join-Path $OutDir 'cpu.json'
$json | Out-File -FilePath $outFile -Encoding utf8

# optional: print status to console
Write-Output "[$timestamp] CPU: $cpu% -> $outFile"
