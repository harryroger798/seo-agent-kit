# Notion setup helper.
# Opens the Notion integrations page, asks for the token and database ID in
# local GUI dialogs, writes them to .env (gitignored), then runs the importer.
# The token is never printed to the console or sent to chat.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "Opening Notion integrations..."
Start-Process "https://www.notion.so/my-integrations"

Add-Type -AssemblyName Microsoft.VisualBasic

$token = [Microsoft.VisualBasic.Interaction]::InputBox(
  "1. Create an integration named 'SEO Agent Kit'.`n2. Copy the Internal Integration Secret.`n3. Share the directory database with the integration (Connections).`n`nPaste the token here. It starts with secret_ or ntn_. It will be written to .env and never sent to chat.",
  "Notion token"
)
if ([string]::IsNullOrWhiteSpace($token)) {
  Write-Host "Cancelled."
  exit 1
}

$db = ""
if ($token -match "NOTION_DATABASE_ID=") {
  $parts = $token -split "NOTION_DATABASE_ID=", 2
  $token = $parts[0].Trim()
  $db = $parts[1].Trim()
}
if ([string]::IsNullOrWhiteSpace($db)) {
  $db = [Microsoft.VisualBasic.Interaction]::InputBox(
    "Paste the 32-character database ID from the Notion database URL.`nIt is the part before ?v=...",
    "Notion database ID"
  )
}
if ([string]::IsNullOrWhiteSpace($db)) {
  Write-Host "Cancelled."
  exit 1
}

$envPath = Join-Path $root ".env"
$lines = @()
if (Test-Path $envPath) {
  $lines = Get-Content $envPath
}
$lines = $lines | Where-Object {
  $_ -notmatch '^\s*NOTION_TOKEN\s*=' -and $_ -notmatch '^\s*NOTION_DATABASE_ID\s*='
}
$lines += "NOTION_TOKEN=$($token.Trim())"
$lines += "NOTION_DATABASE_ID=$($db.Trim())"
Set-Content -Path $envPath -Value $lines -Encoding ASCII

Write-Host "Credentials written to .env (gitignored)."
Write-Host "Running importer..."
python scripts\import_notion_directories.py --site aliasbrowser.com
