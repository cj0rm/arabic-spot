$ErrorActionPreference = "Stop"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$target = Join-Path $HOME ".agents\skills\arabic-spot"
if (Test-Path $target) {
    throw "Arabic spot already exists at $target. Back it up or remove it first."
}
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
Copy-Item -Path $root -Destination $target -Recurse
$gitFolder = Join-Path $target ".git"
if (Test-Path $gitFolder) { Remove-Item $gitFolder -Recurse -Force }
Write-Host "Arabic spot installed at $target"
Write-Host 'In Codex, try: $arabic-spot اكتب قصيدة عن عُمان'
