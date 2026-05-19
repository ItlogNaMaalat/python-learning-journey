# Git & GitHub Beginner Guide

A beginner-friendly guide for learning the basic Git workflow and using GitHub to manage coding projects and track development progress.

---

# What is Git?

Git is a version control system used to:
- track code changes
- save project versions
- manage files
- restore older versions
- organize development workflow

Think of Git as:
> a save/checkpoint system for programming projects.

---

# What is GitHub?

GitHub is an online platform where Git repositories are stored.

GitHub is used to:
- upload projects online
- build a coding portfolio
- store backups
- collaborate with other developers
- document coding progress

---

# Basic Git Workflow

```bash
git add .
git commit -m "your message"
git push
```

This is the standard workflow developers use after coding.

---

# Step 1 — Initialize Git Repository

```bash
git init
```

Creates a Git repository inside the current project folder.

Use this once when starting a new project.

---

# Step 2 — Check Project Status

```bash
git status
```

Shows:
- modified files
- untracked files
- staged files
- files ready to commit

Good habit:
> Always check status before committing.

---

# Step 3 — Add Changes (Stage Files)

## Add all files

```bash
git add .
```

Stages all modified and new files inside the current folder.

Meaning:
> prepare all changes for the next commit.

---

## Add specific file only

```bash
git add practice.py
```

Stages only the selected file.

Useful when:
- only one file is finished
- other files are incomplete
- you want cleaner commits

---

## Files with spaces

Use quotation marks:

```bash
git add "Day 5 - Functions/exercise1.py"
```

Without quotation marks, Git may treat spaces as separate arguments.

---

# Step 4 — Commit Changes (Save Version)

```bash
git commit -m "your message"
```

Creates a saved version/checkpoint of staged files.

Example:

```bash
git commit -m "Finished Day 5 exercises"
```

A commit message explains:
> what changes were made.

---

# Step 5 — Upload to GitHub

```bash
git push
```

Uploads committed changes from the local repository to GitHub.

Meaning:
> send saved work online.

---

# Download Updates from GitHub

```bash
git pull
```

Downloads and syncs the latest updates from GitHub to the local repository.

Useful when:
- using multiple devices
- repository changed online
- collaborating with others

---

# Understanding Git File States

| State | Meaning |
|---|---|
| Untracked | New file not tracked by Git |
| Modified | Existing file was changed |
| Staged | Ready to commit |
| Committed | Saved into Git history |

---

# Common Git Commands

| Command | Purpose |
|---|---|
| `git init` | Start Git repository |
| `git status` | Check project status |
| `git add .` | Stage all files |
| `git add filename` | Stage specific file |
| `git commit -m "message"` | Save version |
| `git push` | Upload to GitHub |
| `git pull` | Download updates |

---

# Daily Git Workflow

Every time after coding:

```bash
git status
git add .
git commit -m "what you did"
git push
```

Example:

```bash
git commit -m "Added loops exercises"
```

---

# Important Beginner Notes

## Git only pushes committed files

Files must first be:
1. added
2. committed

before they can be uploaded.

---

## Commit regularly

Good developers commit often because it:
- tracks progress
- prevents losing work
- keeps project history organized

---

# Developer Mindset

Git is not only for uploading files.

It helps developers:
- organize projects
- track learning progress
- build portfolios
- manage coding history
- work professionally
- collaborate with teams

Learning Git early is one of the best habits in software development.