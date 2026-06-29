Here are some of the most commonly used Git commands:

### Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```

### Create & Clone Repositories

```bash
git init                    # Initialize a new repository
git clone <repo-url>        # Clone a repository
```

### Check Status

```bash
git status                  # Show working tree status
git log                     # View commit history
git log --oneline           # Compact commit history
```

### Add & Commit Changes

```bash
git add <file>              # Stage a file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
```

### Branching

```bash
git branch                  # List branches
git branch <branch-name>    # Create a branch
git checkout <branch-name>  # Switch branch
git switch <branch-name>    # Modern way to switch
git checkout -b <branch>    # Create and switch
git switch -c <branch>      # Create and switch (modern)
```

### Remote Repositories

```bash
git remote -v               # View remotes
git remote add origin <url> # Add remote repository
git push origin main        # Push changes
git pull origin main        # Fetch and merge changes
git fetch                   # Fetch changes only
```

### Merging & Rebasing

```bash
git merge <branch-name>     # Merge branch into current branch
git rebase <branch-name>    # Rebase current branch
```

### Undo Changes

```bash
git restore <file>          # Discard unstaged changes
git reset HEAD <file>       # Unstage a file
git reset --hard HEAD       # Discard all local changes
git revert <commit-id>      # Revert a commit
```

### Stashing

```bash
git stash                   # Save uncommitted changes
git stash list              # List stashes
git stash pop               # Restore latest stash
```

### Tags

```bash
git tag                     # List tags
git tag v1.0                # Create a tag
git push origin v1.0        # Push a tag
```

### Useful Daily Workflow

```bash
git status
git add .
git commit -m "Describe changes"
git pull origin main
git push origin main
```

If you're a beginner, I can also provide a **Git cheat sheet with 20 commands explained in simple terms**.
