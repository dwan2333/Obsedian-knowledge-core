# Git & GitHub Notes

---

## 1. What is Git and GitHub?

**Git** is a distributed version control system that tracks changes to files over time. It lets you save snapshots of your project (called commits), revert to earlier versions, and work on separate features in parallel using branches — all stored locally on your machine.

**GitHub** is a cloud-based platform that hosts Git repositories remotely. It adds collaboration tools on top of Git: pull requests, issue tracking, and team access controls. The key distinction — **Git is the tool, GitHub is the hosting service.**

---

## 2. Git Index & Object Store (Core Internals)

### The Object Store

The object store is Git's permanent database, stored in `.git/objects/`. Every piece of data Git tracks is stored as one of four object types:

- **Blob** — the raw content of a file (no filename, just data)
- **Tree** — a snapshot of a directory, mapping filenames to blobs
- **Commit** — a pointer to a tree + metadata (author, message, parent commit)
- **Tag** — a named pointer to a specific commit

Once an object is written, it is **immutable** — it can never be changed. This is what makes Git's history tamper-proof.

### The Index (Staging Area)

The index is a binary file at `.git/index` — a middle layer between your working directory and the object store.

```
Working Directory  →  git add  →  Index (Staging)  →  git commit  →  Object Store
```

### Why Does the Index Exist? Why Not Commit Directly?

Without the index, every commit would capture *everything* in your working directory — every half-finished change, every experimental edit, every file you touched but didn't mean to include. You would lose the ability to shape your commits.

The index exists to give you **control over what goes into each commit:**

- **Selective staging** — you might have changed 5 files, but only 2 are related to the bug fix you're committing. The index lets you stage just those 2 and commit them cleanly, while the other 3 stay in your working directory for a separate commit later.
- **Reviewing before committing** — the index acts as a checkpoint. You stage changes, inspect them with `git diff --cached`, and only commit when you're satisfied. Without this step, mistakes go straight into history.
- **Building commits incrementally** — you can stage parts of your work over time, assembling a coherent commit piece by piece, rather than being forced to commit everything at once.
- **Separating "save" from "record"** — saving a file to disk (working directory) is not the same as recording it in history (object store). The index is the deliberate act in between — your declaration that "this specific set of changes is ready to become permanent."

**In short:** the object store is permanent and immutable. Committing directly to it with no staging step would be like publishing a book with no editing phase — every draft mistake becomes permanent history. The index is your editing desk.

---

## 3. Git Commands

### `git init`

Initializes a new Git repository in the current folder. Creates the hidden `.git/` directory where all version history and configuration is stored.

```bash
git init
```

### `git add`

Moves file changes from your working directory into the index (staging area), marking them to be included in the next commit.

```bash
git add filename.md      # stage a specific file
git add .               # stage all changes in current directory
```

### `git commit -m 'message'`

Takes everything currently in the index and saves it as a permanent snapshot in the object store. The `-m` flag lets you write the commit message inline.

```bash
git commit -m "Add treasury bonds guide"
```

### `git mv <file> <new-name>`

Renames or moves a file and automatically stages the change — equivalent to renaming the file manually and running `git add`. Keeps Git's history intact.

```bash
git mv old_name.md new_name.md
```

### `git rm <file>`

Removes a file from both your working directory **and** the index. The deletion is staged and will be recorded in the next commit.

```bash
git rm filename.md
```

### `git rm --cached <file>`

Removes a file from the index (stops tracking it) **without** deleting it from your working directory. Useful when you accidentally staged a file you don't want Git to track (e.g., a `.env` file).

```bash
git rm --cached secret.env
```

### `git status`

Shows the current state of your working directory and index. It reports three zones:

| Section | What it means |
|---|---|
| **Changes to be committed** | Files in the index, staged and ready for the next commit |
| **Changes not staged for commit** | Files Git tracks but that have been modified since the last stage |
| **Untracked files** | Files Git has never seen before — not in the index or history |

```bash
git status
```
