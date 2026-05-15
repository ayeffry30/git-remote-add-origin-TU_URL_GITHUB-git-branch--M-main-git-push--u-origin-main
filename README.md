# git-remote-add-origin-TU_URL_GITHUB-git-branch--M-main-git-push--u-origin-main

## Getting Started

This repository is set up and connected to GitHub. Below are the standard git commands used to link a local repository to a remote GitHub repository and push your code.

## Connecting a Local Repository to GitHub

```bash
# Add the remote origin (replace with your actual GitHub repository URL)
git remote add origin YOUR_GITHUB_URL

# Rename the default branch to main
git branch -M main

# Push your code to GitHub and set the upstream tracking branch
git push -u origin main
```

### What each command does

- `git remote add origin <URL>` — Links your local repository to a remote GitHub repository.
- `git branch -M main` — Renames the current branch to `main`.
- `git push -u origin main` — Pushes the `main` branch to GitHub and sets it as the default upstream branch for future `git push` and `git pull` commands.
