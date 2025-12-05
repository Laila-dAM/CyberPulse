# collect_logs.ps1
# Coleta de logs avançada (Sistema + Aplicativo)
# Níveis: Critical, Error, Warning
# Output: output/logs.json

$OutputDir = "$PSScriptRoot/output"
if (!(Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

# Função utilitária para coletar logs
function Get-LogData {
    param (
        [string]$LogName,
        [int[]]$Levels
    )

    Get-WinEvent -LogName $LogName -MaxEvents 200 |
        Where-Object { $Levels -contains $_.Level } |
        Select-Object -First 50 |
        ForEach-Object {
            [PSCustomObject]@{
                TimeCreated = $_.TimeCreated
                Level       = $_.LevelDisplayName
                Id          = $_.Id
                Source      = $_.ProviderName
                Message     = $_.Message
            }
        }
}

Write-Host "[LOGS] Coletando eventos avançados..."

$Data = [PSCustomObject]@{
    timestamp = (Get-Date).ToString("o")
    system = @{
        critical = Get-LogData -LogName "System" -Levels 1
        error    = Get-LogData -LogName "System" -Levels 2
        warning  = Get-LogData -LogName "System" -Levels 3
    }
    application = @{
        critical = Get-LogData -LogName "Application" -Levels 1
        error    = Get-LogData -LogName "Application" -Levels 2
        warning  = Get-LogData -LogName "Application" -Levels 3
    }
}

$OutputFile = "$OutputDir/logs.json"
$Data | ConvertTo-Json -Depth 6 | Set-Content $OutputFile -Encoding UTF8

Write-Host "[LOGS] Exportado para $OutputFile"
