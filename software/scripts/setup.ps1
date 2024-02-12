#!/usr/bin/env pwsh

$_scripts = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
$_repo = (Get-Item $_scripts).parent.fullname

Import-Module "$_scripts\lib\utilities.psm1"

#$env:CI = "true"
# ------------------------------------------------------------------------------

Test-IfNotCI { Write-Host "Not in CI" }

Write-Host "Not yet implemented"
