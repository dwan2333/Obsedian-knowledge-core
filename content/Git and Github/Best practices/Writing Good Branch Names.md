# Writing Good Branch Names

A good branch name tells you (and your CI pipeline, and your teammates) **what's being worked on and what kind of change it is** at a glance. The same `git log --oneline` discipline that makes commit messages scannable applies to branch names — keep them lowercase, prefix-tagged, and descriptive enough that `git branch | grep feature/` is useful.

This note covers the consensus structural rules and the prefix vocabulary that's effectively standard across teams.

---

## The Format

Branch names follow this shape:

```
<type>/<short-description>
<type>/<ticket-id>-<short-description>     # with issue tracker
<author>/<type>/<short-description>         # optional author prefix
```

Examples:

| Branch | What it is |
|---|---|
| `feature/login-system` | New feature, no ticket |
| `feature/AUTH-142-add-jwt-login` | Feature tied to ticket AUTH-142 |
| `bugfix/null-session-on-logout` | Non-critical bug fix |
| `hotfix/security-patch` | Emergency production fix |
| `release/v2.0.1` | Release preparation |
| `docs/update-readme-screenshots` | Documentation only |
| `johndoe/feature/profile-page` | With author prefix (some teams) |

Long-lived branches like `main`, `master`, `dev`, `qa`, and `staging` typically use no prefix — they're the platform, not the work.

---

## The Rules

The five rules every source agrees on:

1. **Lowercase only.** No `Feature/Login` — it should be `feature/login`.
2. **Hyphens to separate words within a segment.** `add-login-button`, not `add_login_button` or `addLoginButton`.
3. **Slashes to separate sections.** `feature/T-123-add-login` keeps the type, ticket, and description visually grouped.
4. **Only `a-z`, `0-9`, `-`, and `/`.** No spaces (most tooling rejects them), no `@`, `#`, `!`, no underscores.
5. **No consecutive hyphens, no trailing hyphens, no leading hyphens.** `feature--login` and `feature-login-` both break tooling.

> [!tip] Why no spaces in branch names
> Git accepts spaces if you escape them in shell commands, but most tooling (GitHub Actions, automated linters, branch-protection rules) parses branches as URL-safe slugs. A space breaks the parse silently — your CI job won't trigger and you won't get an error.

---

## The Standard Prefix Vocabulary

| Prefix | When to use |
|---|---|
| **`feature/`** | A new feature being developed |
| **`bugfix/`** | Non-critical bug fix |
| **`hotfix/`** | Emergency production fix |
| **`release/`** | Preparing a tagged release |
| **`docs/`** | Documentation-only change |
| **`chore/`** | Maintenance, deps, build tweaks |
| **`test/`** | Adding or fixing tests |
| **`refactor/`** | Code restructuring without behavior change |
| **`wip/`** | Work in progress, not ready for review |
| **`experimental/`** | Throwaway exploration |

These mirror the Conventional Commits type vocabulary deliberately. If your team uses `feat:` in commits, using `feature/` (or `feat/`) in branches keeps the metadata aligned and lets a single regex parse both.

The exact set matters less than **consistency**. A team that uses `feat/` instead of `feature/` is fine — what matters is that every member uses the same set so `git branch | grep feat/` is reliable.

---

## Why the Format Matters

The point isn't aesthetics — machine tooling and humans both lean on it.

- **CI/CD triggers.** GitHub Actions and GitLab CI run different pipelines per branch prefix. `feature/*` deploys to staging; `release/*` triggers a publish job.
- **Branch protection rules.** Force PR review on `release/*` and `hotfix/*` but allow direct push on `feature/*`.
- **Quick filtering.** `git branch | grep hotfix/` shows every emergency fix in flight.
- **Skimmability.** A teammate looking at `git log --oneline --branches` immediately sees what's in flight and what kind of work it is.

---

## Anti-Patterns

| Anti-pattern | Why it's wrong | Better |
|---|---|---|
| `Feature/Login` | Mixed case | `feature/login` |
| `feature--login` | Consecutive hyphens | `feature/login` |
| `feature-login-` | Trailing hyphen | `feature/login` |
| `feature/login screen` | Spaces break tooling | `feature/login-screen` |
| `bugfix/T-123` | No description; what bug? | `bugfix/T-123-fix-null-session` |
| `johns-branch` | No type, vague purpose | `johndoe/feature/add-profile-page` |
| `fix` | One word, no context | `bugfix/fix-login-error` |
| `feature/T-123/sub/T-456-xx` | Too many slashes; over-stacked | `feature/T-456-add-xx` |
| `add_login_button` | Underscores | `feature/add-login-button` |

---

## A Worked Example

Suppose you're working on Jira ticket `AUTH-142` to add JWT login to the authentication module.

**Bad:**

```
fix
my-feature
auth_jwt_branch
Feature/JWT/login
```

**Good:**

```
feature/AUTH-142-add-jwt-login
```

This single branch name tells the reader:

- *Type:* feature (a new capability, not a bug fix)
- *Ticket:* AUTH-142 (linkable to your project tracker)
- *Subject:* add JWT login (specific, imperative-mood)

When you run `git push -u origin feature/AUTH-142-add-jwt-login`, GitHub auto-suggests a PR title from the branch name — and the suggested title is already in shape for a Conventional Commits subject.

---

## Related Documents

- **[[Writing Good Commit Messages]]** — sibling best practice; same imperative-mood discipline applied to commit subjects
- **[[Branching (Main)]]** — the mechanics of `git branch`, switching, deleting
- **[[GitHub pull request]]** — PR titles often inherit from branch names

---

## Sources

| Source | Type |
|---|---|
| [Conventional Branch — naming spec](https://conventional-branch.github.io/) | Standard (Conventional Commits' branch sibling) |
| [Git Branch Naming Convention — phoenixNAP](https://phoenixnap.com/kb/git-branch-name-convention) | Tutorial |
| [Naming Conventions for Git Branches — Abhay Amin (Medium)](https://medium.com/@abhay.pixolo/naming-conventions-for-git-branches-a-cheatsheet-8549feca2534) | Cheatsheet |
