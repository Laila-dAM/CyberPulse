
try {
    # Alguns sistemas expõem temperatura via Win32_PerfFormattedData
    $tempData = Get-CimInstance -Namespace root/cimv2 -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation -ErrorAction Stop

    $temperature = $tempData.Temperature
    # Ajuste: alguns sensores retornam 10x maior
    if ($temperature -gt 200) {
        $temperature = [math]::Round($temperature / 10, 1)
    }

    $status = "OK"
}
catch {
    # Sensor não disponível
    $temperature = $null
    $status = "Sensor indisponível"
}

$result = @{
    Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    Temperature = $temperature
    Status = $status
}

$outPath = "$PSScriptRoot/output/temp.json"
$result | ConvertTo-Json | Set-Content $outPath

Write-Host "[TEMP] $status -> $outPath"
