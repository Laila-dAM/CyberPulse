
$OutputDir = "$PSScriptRoot/output"
$BackendUrl = "http://localhost:3000/metrics"   # ajuste se necessário

Write-Host "[SEND] Lendo arquivos JSON em $OutputDir..."

if (!(Test-Path $OutputDir)) {
    Write-Host "[SEND] ERRO: Pasta output/ não existe."
    exit
}

$Files = Get-ChildItem -Path $OutputDir -Filter *.json

if ($Files.Count -eq 0) {
    Write-Host "[SEND] ERRO: Nenhum arquivo JSON encontrado em output/"
    exit
}

$Payload = @{}

foreach ($File in $Files) {
    try {
        $JsonContent = Get-Content $File.FullName -Raw | ConvertFrom-Json
        $KeyName = [System.IO.Path]::GetFileNameWithoutExtension($File.Name)
        $Payload[$KeyName] = $JsonContent
        Write-Host "[SEND] + Adicionado: $($File.Name)"
    }
    catch {
        Write-Host "[SEND] ERRO ao ler $($File.Name): $_"
    }
}

Write-Host "[SEND] Enviando métricas para o backend $BackendUrl ..."

try {
    $Response = Invoke-RestMethod -Uri $BackendUrl -Method Post -Body ($Payload | ConvertTo-Json -Depth 10) -ContentType "application/json"
    Write-Host "[SEND] Sucesso! Resposta:"
    Write-Host $Response
}
catch {
    Write-Host "[SEND] ERRO ao enviar métricas:"
    Write-Host $_
}
