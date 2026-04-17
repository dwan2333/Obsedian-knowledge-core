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

---

## `git log`

Shows the commit history of the current branch — each commit's hash, author, date, and message, with the newest at the top. Useful for reviewing what's been done and finding the commit hash you need for other commands.

```bash
git log                       # full history with author, date, message
git log --oneline             # condensed — one commit per line
git log --graph --oneline     # visual branch graph
git log -n 5                  # show only the last 5 commits
git log -- filename.md        # history filtered to one file
```

## `git show`

Displays everything about a single commit — the commit metadata (hash, author, date, message) **and** the full diff of what that commit changed. If you don't pass a hash, it shows the most recent commit (`HEAD`).

```bash
git show                      # show the most recent commit
git show a1b2c3d              # show a specific commit by hash
git show HEAD~2               # show the commit 2 steps before HEAD
git show a1b2c3d -- file.md   # show only one file's changes in that commit
```

## `git diff`

Shows the differences between two states of your files. By default, it compares your **working directory** against the **index** — in other words, changes you've made but haven't staged yet.

```bash
git diff                     # unstaged changes (working dir vs index)
git diff filename.md         # diff for a specific file only
git diff HEAD                # everything different from the last commit (staged + unstaged)
git diff branch1..branch2    # compare two branches
```

### `git diff --cached` (same as `--staged`)

Shows the differences between the **index** and the **last commit** — what will be included in your next commit if you ran `git commit` right now. This is the counterpart to plain `git diff`, which only shows unstaged changes.

| Command | Compares | Answers the question |
|---|---|---|
| `git diff` | Working dir ↔ Index | What have I changed but not staged? |
| `git diff --cached` | Index ↔ Last commit | What have I staged for the next commit? |
| `git diff HEAD` | Working dir ↔ Last commit | What's different from the last commit in total? |

```bash
git diff --cached             # staged changes only
git diff --staged             # identical — same command, different flag name
```

## `git restore --staged <file>`

Removes a file from the index (unstages it) **without** changing the file's contents in your working directory. Useful when you ran `git add` on something by mistake — the changes are still there, just no longer lined up for the next commit.

```bash
git restore --staged file.md   # unstage a single file
git restore --staged .         # unstage everything currently staged
```

Compare to `git rm --cached`, which stops tracking the file entirely. `git restore --staged` only undoes the most recent `git add` — the file remains tracked.

---

## `git branch`

Lists, creates, or deletes branches. With no arguments, it lists all local branches and marks the current one with an asterisk. Creating a branch with `git branch <name>` makes the branch but does **not** switch to it — use `git switch` for that.

```bash
git branch                     # list all local branches (* marks current)
git branch -a                  # list local + remote branches
git branch feature-x           # create a new branch called feature-x
git branch -d feature-x        # delete a branch (safe — refuses if unmerged)
git branch -D feature-x        # force-delete a branch (even if unmerged)
git branch -m old-name new     # rename a branch
```

## `git switch`

Switches from your current branch to a different one. Replaces the branch-switching role of the older `git checkout` command, which was overloaded with too many unrelated jobs. Safer and more explicit.

```bash
git switch main                # switch to an existing branch
git switch -c feature-x        # create a new branch AND switch to it in one step
git switch -                   # switch back to the previous branch (like `cd -`)
```

| Command | What it does |
|---|---|
| `git branch feature-x` | Creates the branch, stays where you are |
| `git switch feature-x` | Switches to an existing branch |
| `git switch -c feature-x` | Creates AND switches in one step (most common) |
