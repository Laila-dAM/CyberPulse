
$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ss")

$disk = Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='C:'"

$total = [math]::Round($disk.Size / 1GB, 2)
$free  = [math]::Round($disk.FreeSpace / 1GB, 2)
$used  = [math]::Round($total - $free, 2)
$percent = [math]::Round(($used / $total) * 100, 2)

# Cria objeto JSON
$data = @{
    timestamp = $timestamp
    total_gb = $total
    used_gb = $used
    free_gb = $free
    usage_percent = $percent
}

# Garante que a pasta output existe
$outputDir = Join-Path $PSScriptRoot "output"
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# Caminho do JSON final
$outputPath = Join-Path $outputDir "disk.json"

# Salva o JSON formatado
$data | ConvertTo-Json | Out-File -Encoding utf8 $outputPath

Write-Host "[DISK] $percent% used -> $outputPath"
