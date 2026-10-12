# AGENTS.md: rules for Daniel's Knowledge core vault

This is Daniel's **reading vault for mathematics and finance**. Everything here is for him to read: neat, clear, easy to follow. It is published as a public website, so treat every note as public.

Read this whole file before changing anything here.

## 1. Daniel's three vaults

| Vault | Folder | What it's for |
|---|---|---|
| **Knowledge core** (this one) | `E:\Knowledge core` | Math and finance notes he reads. Public website: https://dwan2333.github.io/Obsedian-knowledge-core/ |
| **Coding core** | `E:\Coding core` | Coding and algorithms notes he reads. Also a public website |
| **Brain** | `E:\AI Brain\Big Brain\Brain` | The agent's private memory of Daniel: his profile, preferences, every question, progress data. Private GitHub repo. Never copy Brain data into this vault |

- **Study questions:** best asked in a session opened in the Brain folder, which logs and files them automatically. If he asks one in a session opened here, answer it, save it as a question note (§5), and record it in the Brain by following `E:\AI Brain\Big Brain\Brain\AGENTS.md` §3.
- **Outdated skill:** don't use the `vault-note-creator` skill. Daniel retired it; it conflicts with these rules.

## 2. Layout

- **Published notes:** everything published lives in `content\`. Repo-root files (this one, `quartz\`, `.github\`) are not published.
- **Home page:** `content\index.md`. When you add a new subject area, update its "Sections" list.
- **Folders:** `content\<Category>\<Topic>\…`. Categories are `Mathematics` and `Finance`. Folder names are short Title Case words.
- **Overview notes:** a topic's overview note is named `<Title> (Main).md`.
- **Series notes:** number them in reading order: `1 - Short Title.md`, `2 - Short Title.md`, …
- **Textbooks:** a topic that follows a textbook gets a book folder with chapter folders, e.g. `Mathematics\Linear Algebra\Linear Algebra and Its Applications, Fifth Edition\Chapter 1\`.

## 3. Writing rules (they keep Obsidian and the website both working)

- **File names:** readable Title Case words, because his sidebar shows file names. Never use underscores or snake_case for notes.
  - No `\ / : * ? " < > | # %`, and no dots except before the extension. GitHub Pages can misread `name.with.dots`.
  - Every file name must be unique across the vault.
- **Links:** use the bare file name, `[text](<File Name.md>)`, with angle brackets when it has spaces. Add `#Heading` to link to a section.
  - **Never** use `../` or folder paths: the website resolves links by unique file name, and folder paths give "page not found".
  - Some older notes still have `../` links. If you edit one of those notes, fix its links.
- **Images:** keep each image in the same folder as its note and embed it by bare name: `![alt](<image name.png>)`.
- **Math:** LaTeX: `$…$` inline, and display math on its own lines between `$$` lines.
- **Money:** write the dollar sign as `&#36;` (`&#36;86.62`). A bare `$` is read as the start of math, which breaks the page.
- **Diagrams:** PNG files next to the note, made with a matplotlib `_gen_*.py` script kept beside them. Don't use Mermaid.
- **Callouts:** Mathematics notes use them for structure, e.g. `> [!definition]`, `> [!example]`, `> [!tip]`, `> [!info]`.
- **Changing existing notes:** don't move, rename or delete his notes unless he asks. If you rename a file, update every link to it in the same change.

## 4. Git and publishing

- **Asking first:** the GitHub repo (`dwan2333/Obsedian-knowledge-core`) is **public**, and pushing to `main` publishes the website. Commit or push only when Daniel asks.
- **Commits:** commit only the files you changed. Never sweep in unrelated `.obsidian/` or `.smart-env/` state.
- **Network:** GitHub needs his local proxy, `HTTPS_PROXY=http://127.0.0.1:7897`. Don't bypass the proxy; that fails. There is no `gh` command on this PC.
- **His backup:** his Obsidian Git plugin also commits and pushes ("vault backup: …").
- **Site settings:** `quartz.config.ts` controls the site. Don't change it without asking.
- **Python on Windows:** run `python`, not `py`. The `py` launcher is broken in some of his terminals.

## 5. Question notes ("Questions I Had While Studying")

Each study question Daniel asks gets one readable note, filed in that topic's chapter folder if it follows a textbook, otherwise in the topic folder:
`…\<Topic>[\<Book>\Chapter N]\Questions I Had While Studying\YYYY-MM-DD - Short Title.md`

If he sent a screenshot, save it next to the note under the same name. Use `python "E:\AI Brain\Big Brain\Brain\system\save_screenshot.py" --dest "<folder>" --name "<note name>"`, then look at the image to confirm it's his.

**One note per question, kept compact.** Follow-up questions about the same question or topic do **not** get a new note. Update the existing note so it captures the whole question, including every sub-question he asked, as one well-compacted summary:
- add only what's new, merged where it belongs (a new case, angle, example, or a short "Follow-up" callout);
- update the Question Essence to cover it;
- never repeat what the note already says.

Start a new note only for a genuinely new question.

**Format: match his textbook notes** (house style; see `Chapter 2 (Main).md` and `Chapter 1 Exercises.md` under `Introduction to Probability` for models). The example note is `2026-10-12 - Proving the 2x2 inverse formula.md` in Linear Algebra's `Chapter 2\Questions I Had While Studying`.

```
# <Exercises 25–26 / short topic> — <Title in Title Case>

_Question I had while studying · <book, §section> · asked YYYY-MM-DD_

---

> [!info] Question Essence
> <3–5 sentences: what was asked (every sub-question) and the core idea of the answer>

---

## The Question
![<book § and exercise>](<YYYY-MM-DD - Short Title.png>)    ← if there is no screenshot, state the question here instead

---

## The Result Being Proved          ← when a theorem/definition is involved
> [!definition] Theorem N (§x.y) — <name>
> <statement, with LaTeX>

---

## Exercise N — <what it shows>     ← one section per exercise or sub-question
> [!example] Exercise N — <short name>
> **Problem.** <the problem, verbatim>
>
> > [!success]- Click to reveal solution
> > **Setup.** … **Solution.** … (cases, steps, display math) **Answer.** … ✓ **Insight.** …

---

## Other Ways to See It
> [!tip] Geometric — …     > [!example] By example     > [!warning] Watch out

---

> [!tip] Key Takeaway
> <one or two lines>

---

## Related Documents
- **[Note Title](<File Name.md>)** — one line on how it connects.
```

- **Sections:** skip any section that doesn't apply. Use separators (`---`) between sections, as his notes do.
- **No repetition:** each idea appears exactly once.
