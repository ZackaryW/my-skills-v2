#!/usr/bin/env bash
# Update Skills Repository Script
# Pulls latest changes from git remote and detects context changes

set -e

REPO_PATH="${1:-}"

get_file_hash() {
    local path="$1"
    if [ -f "$path" ]; then
        if command -v md5sum >/dev/null 2>&1; then
            md5sum "$path" | cut -d' ' -f1
        elif command -v md5 >/dev/null 2>&1; then
            md5 -q "$path"
        else
            echo ""
        fi
    else
        echo ""
    fi
}

update_single_repo() {
    local path="$1"
    local repo_name=$(basename "$path")
    
    echo ""
    echo -e "\033[36mUpdating repository: $repo_name\033[0m"
    
    # Check if it's a git repo
    if [ ! -d "$path/.git" ]; then
        echo -e "  \033[33mNot a git repository - skipping\033[0m"
        return 1
    fi
    
    # Hash about.md before pull
    local about_path="$path/about.md"
    local hash_before=$(get_file_hash "$about_path")
    
    # Pull updates
    echo -e "  \033[90mRunning git pull...\033[0m"
    if (cd "$path" && git pull 2>&1); then
        echo -e "  \033[32m✓ Updated successfully\033[0m"
        
        # Check if about.md changed
        local hash_after=$(get_file_hash "$about_path")
        if [ -n "$hash_before" ] && [ -n "$hash_after" ] && [ "$hash_before" != "$hash_after" ]; then
            echo -e "  \033[33m⚠️  about.md changed - refresh your AI context!\033[0m"
            echo -e "     \033[33mRe-read about.md to get updated instructions\033[0m"
        fi
        return 0
    else
        echo -e "  \033[31m✗ Pull failed\033[0m"
        return 1
    fi
}

update_skills_group() {
    local group_path="$1"
    
    echo ""
    echo -e "\033[36mUpdating skills group: $group_path\033[0m"
    
    if [ ! -d "$group_path" ]; then
        echo -e "  \033[31mGroup directory not found\033[0m"
        return
    fi
    
    local updated=0
    local skipped=0
    
    for dir in "$group_path"/*; do
        if [ -d "$dir" ]; then
            if update_single_repo "$dir"; then
                ((updated++))
            else
                ((skipped++))
            fi
        fi
    done
    
    echo ""
    echo -e "\033[36mSummary: $updated updated, $skipped skipped\033[0m"
}

# Main logic
echo -e "\033[36mSkills Repository Updater\033[0m"
echo -e "\033[36m=========================\033[0m"

# Resolve repository path
if [ -z "$REPO_PATH" ]; then
    if [ -n "$MY_SKILLS_REPO" ]; then
        REPO_PATH="$MY_SKILLS_REPO"
        echo -e "\033[90mUsing MY_SKILLS_REPO: $REPO_PATH\033[0m"
    elif [ -n "$SKILLS_GROUP_DIR" ]; then
        REPO_PATH="$SKILLS_GROUP_DIR"
        echo -e "\033[90mUsing SKILLS_GROUP_DIR: $REPO_PATH\033[0m"
    else
        echo -e "\033[31mError: Neither MY_SKILLS_REPO nor SKILLS_GROUP_DIR is set\033[0m"
        echo -e "\033[33mPlease set one of these environment variables\033[0m"
        exit 1
    fi
fi

if [ ! -d "$REPO_PATH" ]; then
    echo -e "\033[31mError: Path not found: $REPO_PATH\033[0m"
    exit 1
fi

# Determine if single repo or group directory
if [ -d "$REPO_PATH/.git" ]; then
    # Single repository
    update_single_repo "$REPO_PATH"
else
    # Skills group directory
    update_skills_group "$REPO_PATH"
fi

echo ""
echo -e "\033[32mUpdate complete!\033[0m"
