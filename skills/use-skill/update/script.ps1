# Update Skills Repository Script
# Pulls latest changes from git remote and detects context changes

param(
    [string]$RepoPath = $null
)

function Get-FileHashQuick {
    param([string]$Path)
    if (Test-Path $Path) {
        return (Get-FileHash $Path -Algorithm MD5).Hash
    }
    return $null
}

function Update-SingleRepo {
    param([string]$Path)
    
    $repoName = Split-Path $Path -Leaf
    Write-Host "`nUpdating repository: $repoName" -ForegroundColor Cyan
    
    # Check if it's a git repo
    if (-not (Test-Path (Join-Path $Path ".git"))) {
        Write-Host "  Not a git repository - skipping" -ForegroundColor Yellow
        return $false
    }
    
    # Hash about.md before pull
    $aboutPath = Join-Path $Path "about.md"
    $hashBefore = Get-FileHashQuick $aboutPath
    
    # Pull updates
    try {
        Push-Location $Path
        Write-Host "  Running git pull..." -ForegroundColor Gray
        $output = git pull 2>&1
        $success = $LASTEXITCODE -eq 0
        Pop-Location
        
        if ($success) {
            Write-Host "  ✓ Updated successfully" -ForegroundColor Green
            
            # Check if about.md changed
            $hashAfter = Get-FileHashQuick $aboutPath
            if ($hashBefore -and $hashAfter -and ($hashBefore -ne $hashAfter)) {
                Write-Host "  ⚠️  about.md changed - refresh your AI context!" -ForegroundColor Yellow
                Write-Host "     Re-read about.md to get updated instructions" -ForegroundColor Yellow
            }
            
            return $true
        } else {
            Write-Host "  ✗ Pull failed: $output" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Pop-Location
        Write-Host "  ✗ Error: $_" -ForegroundColor Red
        return $false
    }
}

function Update-SkillsGroup {
    param([string]$GroupPath)
    
    Write-Host "`nUpdating skills group: $GroupPath" -ForegroundColor Cyan
    
    if (-not (Test-Path $GroupPath)) {
        Write-Host "  Group directory not found" -ForegroundColor Red
        return
    }
    
    $subdirs = Get-ChildItem $GroupPath -Directory
    $updated = 0
    $skipped = 0
    
    foreach ($dir in $subdirs) {
        if (Update-SingleRepo $dir.FullName) {
            $updated++
        } else {
            $skipped++
        }
    }
    
    Write-Host "`nSummary: $updated updated, $skipped skipped" -ForegroundColor Cyan
}

# Main logic
Write-Host "Skills Repository Updater" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan

# Resolve repository path
if (-not $RepoPath) {
    if ($env:MY_SKILLS_REPO) {
        $RepoPath = $env:MY_SKILLS_REPO
        Write-Host "Using MY_SKILLS_REPO: $RepoPath" -ForegroundColor Gray
    }
    elseif ($env:SKILLS_GROUP_DIR) {
        $RepoPath = $env:SKILLS_GROUP_DIR
        Write-Host "Using SKILLS_GROUP_DIR: $RepoPath" -ForegroundColor Gray
    }
    else {
        Write-Host "Error: Neither MY_SKILLS_REPO nor SKILLS_GROUP_DIR is set" -ForegroundColor Red
        Write-Host "Please set one of these environment variables" -ForegroundColor Yellow
        exit 1
    }
}

if (-not (Test-Path $RepoPath)) {
    Write-Host "Error: Path not found: $RepoPath" -ForegroundColor Red
    exit 1
}

# Determine if single repo or group directory
if (Test-Path (Join-Path $RepoPath ".git")) {
    # Single repository
    Update-SingleRepo $RepoPath
}
else {
    # Skills group directory
    Update-SkillsGroup $RepoPath
}

Write-Host "`nUpdate complete!" -ForegroundColor Green
