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

---

## `git config` — Configuration Levels & Files

Git stores configuration in three files, each scoped to a different level. Narrower scope overrides broader scope:

| Level | Flag | File Location | Scope |
|---|---|---|---|
| **System** | `--system` | `C:\ProgramData\Git\config` (Windows) | All users, all repos on the machine |
| **Global** | `--global` | `C:\Users\<username>\.gitconfig` | All repos for the current OS user |
| **Local** | `--local` (default) | `<repo>/.git/config` | Only the current repository |

**Precedence: local > global > system** — Git starts at local and bubbles up. The most specific value wins.

### Configure Your Identity

Every commit permanently embeds your name and email. Set them globally so they apply to all repos:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

To override for a single repo, run the same commands without `--global` (defaults to `--local`):

```bash
git config user.name "Work Name"
git config user.email "work@company.com"
```

### Configure the Default Branch

Since Git 2.28, you can change the default branch name created by `git init` (previously always `master`):

```bash
git config --global init.defaultBranch main
```

### Remove Config Properties

**Unset a single key:**
```bash
git config --global --unset user.name
```

**Unset all values for a key** (if a key has multiple entries):
```bash
git config --global --unset-all user.name
```

**Remove an entire section:**
```bash
git config --global --remove-section user
```

### View Config

```bash
git config --list            # list all active config values
git config --global --edit   # open global config in your default editor
```
