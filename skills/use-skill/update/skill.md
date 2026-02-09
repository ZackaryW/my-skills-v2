# update

Pull latest changes from skills repository git remote.

## Platform Support
- **Windows**: `script.ps1` (PowerShell)
- **Unix/Linux/Mac**: `script.sh` (bash)

Both scripts provide identical functionality.

## Path Resolution
Resolves repository path using environment variables:
1. `$MY_SKILLS_REPO` (or `$env:MY_SKILLS_REPO` on Windows) — direct path to repo root
2. `$SKILLS_GROUP_DIR/{repo-name}` (or `$env:SKILLS_GROUP_DIR` on Windows) — derive from parent directory

Works identically across all platforms.

## Git Detection
Checks for `.git` directory to determine if path is a git repository.
If `.git` exists at resolved path: single repo update.
If resolved path is a group directory: check each subdirectory for git repos.

## Single Repo Update
For a single repository:
1. Hash `about.md` before pull
2. Execute `git pull`
3. Hash `about.md` after pull
4. Compare hashes to detect changes

## Group Update
For skills group directory:
Iterate immediate subdirectories, update each git repository independently.
Skip non-git directories.

## Context Refresh
If `about.md` changes after pull:
- Agent should re-read the instruction file
- User should refresh context in their AI assistant
- Notification is displayed to user

## Usage
```powershell
# Windows (PowerShell)
use-skill/update
# or
.\skills\use-skill\update\script.ps1
```

```bash
# Unix/Linux/Mac (bash)
use-skill/update
# or
./skills/use-skill/update/script.sh
```
