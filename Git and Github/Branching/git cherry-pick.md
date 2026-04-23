# `git cherry-pick` — Apply Specific Commits Anywhere

`git cherry-pick` takes one or more existing commits by their SHA and **replays them onto your current branch** as new commits. Unlike [[git merge]] or [[git rebase]] — which move whole branches of history — cherry-pick surgically copies *individual* commits wherever you want them.

> [!info] A surgical commit transplant
> Merge and rebase deal in branches. Cherry-pick deals in single commits. You pick a commit by its hash, stay on your current branch, and Git produces a **new commit with a new hash** that applies the same diff.

---

## The Idea in One Picture

### Before — a bug fix sits on `feature` but production needs it now

```mermaid
gitGraph
    commit id: "A"
    commit id: "B"
    branch feature
    commit id: "C"
    commit id: "D-bugfix"
    commit id: "E-wip"
```

### After `git cherry-pick D` (from `main`)

```mermaid
gitGraph
    commit id: "A"
    commit id: "B"
    commit id: "D-prime"
    branch feature
    commit id: "C"
    commit id: "D-bugfix"
    commit id: "E-wip"
```

Only commit `D`'s changes landed on `main` — as a new commit `D'` with a different SHA. The rest of `feature` is untouched.

> [!tip] Same diff, new hash
> Every cherry-picked commit is a fresh object. Two commits with identical changes on different branches are **not** the same commit — Git only compares by hash.

---

## Basic Syntax

```bash
git cherry-pick <commit-sha>
```

Find the commit you want with `git log` (or `git log <branch>` for another branch), then run the command from the branch you want to apply it to.

### Multiple commits and ranges

```bash
git cherry-pick <sha1> <sha2> <sha3>     # apply three specific commits in order
git cherry-pick <sha1>..<sha5>           # range: sha1 (exclusive) → sha5 (inclusive)
git cherry-pick <sha1>^..<sha5>          # range: sha1 (inclusive) → sha5 (inclusive)
git cherry-pick ^<sha> <branch>          # all ancestors of <branch> except <sha>
```

Order matters — commits apply in the order given.

---

## Common Use Cases

### 1. Hotfix a bug on `main` from inside a feature branch

You spotted a production bug mid-feature. Fix it as its own commit, pop it over to `main`, and ship:

```bash
# on feature-login — fix and commit the bug in isolation
git commit -m "Fix XSS in login form"
git log -1 --format=%H           # capture the SHA

# copy just that commit to main
git checkout main
git cherry-pick <sha>
git push origin main
```

The feature branch keeps going without interruption, and the fix ships immediately.

### 2. Share a single commit between developers

A teammate built a utility function on their branch. You need only that commit, not the rest of their work:

```bash
git fetch
git cherry-pick origin/colleague-branch~3   # grab the commit 3 behind their tip
```

### 3. Rescue a commit from the wrong branch

You accidentally committed to `main` when you meant `feature-x`:

```bash
git checkout feature-x
git cherry-pick main                        # copy the latest main commit here
git checkout main
git reset --hard HEAD~1                     # remove it from main (local only — don't do this if pushed)
```

### 4. Backport a fix to a long-lived release branch

Ship a fix to maintenance while preserving a trail back to the original:

```bash
git checkout release-2.x
git cherry-pick -x <sha-on-main>
```

The `-x` flag appends *"(cherry picked from commit …)"* to the message. Use it whenever the two branches are both public so collaborators can trace the origin.

---

## Options Reference

| Flag                         | Purpose                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `-e`, `--edit`               | Open the editor to edit the commit message before committing                                                         |
| `-x`                         | Append *"(cherry picked from commit …)"* to the message — recommended when backporting between public branches       |
| `-n`, `--no-commit`          | Apply the changes to the working tree + index but **don't create a commit** — useful for combining several picks     |
| `-s`, `--signoff`            | Add a `Signed-off-by` trailer                                                                                        |
| `-m <n>`, `--mainline <n>`   | Cherry-pick a merge commit — tell Git which parent (1 or 2) is the mainline                                          |
| `-S`, `--gpg-sign`           | GPG-sign the resulting commit                                                                                        |
| `--ff`                       | If HEAD is the parent of the picked commit, fast-forward instead of creating a new commit                            |
| `--allow-empty`              | Preserve an empty (no-diff) cherry-picked commit instead of erroring                                                 |
| `--empty=drop\|keep\|stop`   | Handle commits whose changes are already in your branch — default is `drop`                                          |
| `--strategy=<s>` / `-X<opt>` | Pick a merge strategy (`recursive`, `ours`, `patience`…) or pass a strategy option                                   |

### Mid-sequence control

When a range of cherry-picks hits a conflict, Git pauses between commits. Use these to steer the rest of the sequence:

| Flag         | Purpose                                                          |
| ------------ | ---------------------------------------------------------------- |
| `--continue` | After resolving conflicts, resume the cherry-pick sequence       |
| `--skip`     | Abandon the current commit and continue with the rest            |
| `--abort`    | Cancel the whole operation and return to the pre-pick state      |
| `--quit`     | Forget the in-progress sequencer state without rolling back      |

---

## Cherry-Picking a Merge Commit

A regular cherry-pick fails on a merge commit — Git can't tell which parent's changes you want. Use `-m <n>` to declare the **mainline parent**:

```bash
git cherry-pick -m 1 <merge-sha>     # diff is "merge commit vs. first parent"
git cherry-pick -m 2 <merge-sha>     # diff is "merge commit vs. second parent"
```

Parent numbering follows `git show <sha>` — the first `Merge:` parent is `1`, the second is `2`.

> [!warning] Cherry-picking merges is usually a smell
> If you need a merge's contents elsewhere, it's almost always cleaner to cherry-pick the individual commits that fed into that merge, or to re-merge the source branch.

---

## Handling Conflicts

Cherry-pick uses the same 3-way merge machinery as [[git merge]], so conflicts look identical:

```bash
git cherry-pick <sha>
# CONFLICT (content): Merge conflict in path/to/file

git status                       # list conflicted files
# ...edit files, resolve <<<<<<< / ======= / >>>>>>> markers...
git add <resolved-files>
git cherry-pick --continue       # finish the pick and create the commit

# Or bail out:
git cherry-pick --abort          # undo, back to clean pre-pick state
```

See [[Merge Conflicts]] — the conflict markers and resolution flow are exactly the same as in a merge or rebase.

---

## ⚠ Pitfalls and When NOT to Cherry-Pick

> [!danger] Cherry-pick is a scalpel, not a workflow
> It creates **duplicate commits with different hashes**. If you later merge or rebase the source branch into the same target, Git often can't tell the two are the same — it either applies them twice or forces you through phantom conflicts.

### Specific traps

- **Overuse fragments history.** If the same change ends up on multiple branches via cherry-pick, `git log` becomes hard to read and `git bisect` can blame the wrong commit.
- **Hidden dependencies.** Commit `D` might compile fine because commit `C` introduced a helper. Cherry-picking `D` alone can silently break the target branch.
- **Testing equivalence is an illusion.** A fix that passed tests on `feature` may interact differently with `main`'s code. Cherry-picking skips the integration test that a real merge would force.
- **Multi-environment promotion (dev → staging → prod) by cherry-pick is an anti-pattern.** It means "the code that was tested is not the code that shipped," and the same conflicts have to be resolved in every environment. Prefer promoting whole branches with [[git merge]].

### Rule of thumb

> Use cherry-pick for **one-off, isolated commits** — hotfixes, backports, and rescue operations. For ongoing integration between branches, use [[git merge]] or [[git rebase]] instead.

---

## Cherry-Pick vs Merge vs Rebase — Choosing

| Situation                                         | Prefer                 |
| ------------------------------------------------- | ---------------------- |
| Ship a single fix to `main` mid-feature           | **Cherry-pick**        |
| Backport a fix to a long-lived release branch     | **Cherry-pick** (`-x`) |
| Rescue commits landed on the wrong branch         | **Cherry-pick**        |
| Integrate a completed feature into `main`         | [[git merge]]          |
| Catch a feature branch up with the latest `main`  | [[git rebase]]         |
| Promote a branch through dev → stage → prod       | [[git merge]]          |
| Collapse a noisy feature into one commit          | [[Squashing Commits]]  |

---

## Recovering from a Bad Cherry-Pick

`git reflog` still has your pre-pick HEAD:

```bash
git reflog                       # find the HEAD@{n} before the cherry-pick
git reset --hard HEAD@{n}        # jump back to that state
```

Already committed the pick and want to back it out cleanly?

- **If not pushed:** `git reset --hard HEAD~1` removes the pick.
- **If pushed:** `git revert <sha>` creates an inverse commit, preserving history.

---

## End-to-End Example — Hotfix Workflow

```bash
# You're deep into a feature branch and spot a bug
git checkout feature-payments
# ...fix the bug in its own isolated commit...
git commit -m "Fix currency rounding in order total"

# Capture the SHA
git log -1 --format=%H
# a1b2c3d4...

# Ship it to main without merging the whole feature
git checkout main
git pull --rebase
git cherry-pick -x a1b2c3d4
git push origin main

# Resume feature work — your branch is unaffected
git checkout feature-payments
```

When the feature eventually merges, Git's `--empty=drop` default handles the already-applied commit cleanly — but see the pitfall section for cases where it doesn't.

---

## See Also

- [[Branching (Main)]] — overview of branches and core commands
- [[git merge]] — integrate whole branches instead of single commits
- [[git rebase]] — replay many commits in sequence (`-i` lets you pick/reorder/squash)
- [[Merge Conflicts]] — same conflict markers, same resolution flow
- [[Squashing Commits]] — when you want to combine commits rather than transplant them
- [[git checkout]] — switch to the branch that will receive the pick
- [[Git Essential Commands]] — everyday-command quick-reference
