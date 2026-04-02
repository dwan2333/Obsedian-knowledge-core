# Git Commands

## `git init`

Initializes a new Git repository in the current folder. Creates the hidden `.git/` directory where all version history and configuration is stored.

```bash
git init
```

## `git add`

Moves file changes from your working directory into the index (staging area), marking them to be included in the next commit.

```bash
git add filename.md      # stage a specific file
git add .               # stage all changes in current directory
```

## `git commit -m 'message'`

Takes everything currently in the index and saves it as a permanent snapshot in the object store. The `-m` flag lets you write the commit message inline.

```bash
git commit -m "Add treasury bonds guide"
```

## `git mv <file> <new-name>`

Renames or moves a file and automatically stages the change — equivalent to renaming the file manually and running `git add`. Keeps Git's history intact.

```bash
git mv old_name.md new_name.md
```

## `git rm <file>`

Removes a file from both your working directory **and** the index. The deletion is staged and will be recorded in the next commit.

```bash
git rm filename.md
```

## `git rm --cached <file>`

Removes a file from the index (stops tracking it) **without** deleting it from your working directory. Useful when you accidentally staged a file you don't want Git to track (e.g., a `.env` file).

```bash
git rm --cached secret.env
```

## `git status`

Shows the current state of your working directory and index. It reports three zones:

| Section | What it means |
|---|---|
| **Changes to be committed** | Files in the index, staged and ready for the next commit |
| **Changes not staged for commit** | Files Git tracks but that have been modified since the last stage |
| **Untracked files** | Files Git has never seen before — not in the index or history |

```bash
git status
```
