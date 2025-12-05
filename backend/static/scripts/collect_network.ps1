$net = Get-NetAdapterStatistics | Select-Object -First 1

$result = @{
    Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    BytesReceived = $net.ReceivedBytes
    BytesSent = $net.SentBytes
}

$outPath = "$PSScriptRoot/output/network.json"
$result | ConvertTo-Json | Set-Content $outPath

Write-Host "[NETWORK] RX=$($net.ReceivedBytes) bytes, TX=$($net.SentBytes) bytes -> $outPath"
