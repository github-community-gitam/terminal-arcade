# Contributing to Terminal Arcade

Thanks for being here. This repository is part of **GITHUB Community GITAM**. Whether this is your first pull
request ever or your hundredth, the guide below is everything you need.

**If this is your first time:** the single best place to start is
[docs/how-to-add-a-game.md](docs/how-to-add-a-game.md). It has a complete,
working game you can copy and turn into your own.

---

## Never done this before?

You need exactly two things.

| Thing | How to check |
|---|---|
| **A GitHub account** | Sign in at [github.com](https://github.com). [Sign up](https://github.com/signup) — free, two minutes. |
| **Git on your laptop** | Run `git --version` in a terminal. If it prints a number, you have it. |

If `git --version` says "command not found", install it from
[git-scm.com/downloads](https://git-scm.com/downloads). On a Mac, running
`git --version` may offer to install it for you — say yes.

**First time using Git on this machine?** Run these two lines once, with your
own details:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Skip them and Git stops you at your first commit with `Please tell me who you are`.

### The whole thing, in eight steps

```
1. Pick an issue    ->  comment /claim
2. Fork             ->  your own copy on GitHub
3. Clone            ->  download it to your laptop
4. Branch           ->  git checkout -b fix/issue-12
5. Change one file  ->  in any editor
6. Commit           ->  save the change with a message
7. Push             ->  send it back to GitHub
8. Pull request     ->  ask us to merge it
```

Everything below is those eight steps, slowly. Most people finish their first
one in under twenty minutes.

**You cannot break anything.** You work on your own copy, on a branch, and a
human reads your change before it goes anywhere near the real project.

---

## What this project is

A collection of small games you play in your terminal — Hangman, Tic Tac Toe,
Guess the Number, Rock Paper Scissors — behind one menu. It exists to be a
gentle, genuinely fun first open source project.

**Tech stack:** Python 3.10+. Nothing else. No dependencies, by design.

---

## Setting up locally

**You will need:** Python 3.10 or newer, and Git. That is the whole list.

### Fork it

**Fork** means "make my own copy of this project". Click **Fork** at the top
right of this page, then **Create fork**.

You now have your own copy at `github.com/YOUR-USERNAME/terminal-arcade`. You can do
anything you like to it. **You cannot break the original.**

### Clone your fork

**Clone** means "download my copy so I can open the files".

First check you are on **your fork** — the URL must show *your* username, not
`github-community-gitam`. Then click the green **`< > Code`** button, copy the
HTTPS link, and:

```bash
git clone https://github.com/YOUR-USERNAME/terminal-arcade.git
cd terminal-arcade

# point at the original, so you can pull in other people's merged work later
git remote add upstream https://github.com/github-community-gitam/terminal-arcade.git

# verify: origin must be YOUR username, upstream must be the org
git remote -v
```

> **The single most common mistake.** Cloning the original instead of your fork.
> Everything works until you push, which then fails with **permission denied**.
> `git remote -v` catches it in two seconds.

### Run it

```bash
# there is nothing to install. just:
python3 -m arcade
```

The menu should appear. If it does not, that is a bug in *our* instructions,
not a mistake on your part — open an issue and tell us where it broke.

To run the tests you need pytest, the only package this project ever asks for:

```bash
python3 -m pip install pytest
python3 -m pytest
```

> **Windows:** if `python3` is not found, try `python` or `py`.

---

## The contribution flow

### 1. Find an issue

Browse the [open issues](../../issues):

| Label | Means |
|---|---|
| `good first issue` | No knowledge of the codebase needed |
| `difficulty: beginner` | Small and self-contained |
| `difficulty: intermediate` | You will need to read some existing code |
| `difficulty: advanced` | Involves a design decision |

**Adding a new game** is the easiest starting point, because you are writing a
new file rather than working out how someone else's code fits together.

### 2. Claim it — this step is not optional

Comment `/claim` on the issue. A bot assigns it to you within seconds.

> **PRs on unclaimed issues are closed.** This is not us being strict for the
> sake of it. Without it, six people do the same task and five of them waste
> an evening.

You may hold **2 issues at a time**. Changed your mind? Comment `/unclaim` —
that is completely fine and nobody thinks less of you. Claims go stale after 5
days of no activity and the issue reopens for others.

### 3. Branch

```bash
git checkout main
git pull upstream main
git checkout -b feat/short-description
```

| Prefix | For | Example |
|---|---|---|
| `feat/` | Something new | `feat/coin-flip-game` |
| `fix/` | Something broken | `fix/hangman-repeated-letter` |
| `docs/` | Documentation | `docs/setup-instructions` |
| `test/` | Tests only | `test/scoreboard-sorting` |
| `ci/` | Workflows, linting | `ci/add-python-matrix` |

### 4. Make the change

- Change **only** what the issue asks for
- Match the style of the code around you — look at `arcade/games/guess.py`
- Add a test if you added or fixed logic
- Write docstrings on new functions

**Commit messages:**

```
fix: hangman no longer charges a life for a repeated letter

Closes #23
```

Format: `<type>: <what changed, lowercase, present tense>`, where type is
`feat`, `fix`, `docs`, `test`, `ci`, `refactor`, or `chore`.

### 5. Test before you push

```bash
python3 -m pytest        # all tests must pass
python3 -m arcade        # and play your change, actually play it
```

If you have ruff installed (entirely optional):

```bash
python3 -m pip install ruff
ruff format .          # tidies spacing and quotes
ruff check . --fix     # fixes what it safely can
```

### What can actually fail your pull request

Only two things:

1. **A test fails** — something in `tests/` broke.
2. **A real bug is found** — an undefined variable, an unused import, a mutable
   default argument. The check names the file and the line.

**Formatting never blocks you.** Untidy spacing, single quotes instead of
double, imports in the wrong order, a missing newline at the end of a file —
these show up as suggestions in the log and are then ignored. Your pull request
merges either way.

This is deliberate. A first contribution should not be rejected by a robot over
four spaces of whitespace.

### 6. Open the pull request

```bash
git push origin feat/short-description
```

GitHub then shows a yellow banner on your fork with a
**Compare & pull request** button. Click it, fill in the template, and click
**Create pull request**.

**Your description must contain `Closes #<issue-number>`.** That line links your
work to the issue and closes it automatically when you are merged. Without it
your PR gets sent back, because otherwise issues get forgotten and two people
end up doing the same work.

> If `git push` fails with **permission denied** or **repository not found**, you
> cloned the original instead of your fork. Run `git remote -v` and check whose
> username is there.

**Paste your terminal output.** A few lines showing your game being played, or
the bug no longer happening, makes a reviewer's job trivial and gets you merged
faster than anything else you can do.

### What happens in the first minute

A box appears at the bottom of your pull request with checks running.

**A red X is not a rejection.** It is information. Click **Details** next to the
red one — the log prints the exact command to run on your own machine to see the
same problem.

To fix a red check: change the file, commit, and push to the **same branch**. The
pull request updates itself. You do not open a new one.

### 7. Review

A maintainer responds within **48 hours**:

- **Approved and merged** — done
- **Changes requested** — we leave comments pointing at exact lines. Push more
  commits to the same branch; the PR updates itself. This is normal and happens
  to experienced developers constantly. It is not criticism
- **Closed** — only if the PR breaks a rule below, and we will always say which

---

## Quality standards

We would rather merge 40 real contributions than 400 fake ones. These rules
apply to everyone equally.

### Automatically rejected

Marked `invalid` / `spam` and closed without review:

- Whitespace, comma, or formatting-only changes to Markdown files
- Adding your name or a link to the README without being asked to
- AI-generated code pasted in without being read, that fails the linter or
  ships without tests
- PRs that duplicate an already-open PR
- Renaming variables or "improving" code nobody asked to change
- A PR with no linked issue

### Always welcome

- Fixing a genuine bug, however small
- Adding a missing test
- Rewriting confusing documentation so it is actually clear
- Improving an error message
- Telling us our setup instructions are wrong

### The 48-hour maintainer commitment

We commit to acknowledging every PR within 48 hours. If yours has been sitting
longer, say so in a comment on the pull request — you are not being annoying,
we dropped the ball.

---

## Using AI tools

You may use ChatGPT, GitHub Copilot, or anything else you like.

What you may not do is open a pull request you cannot explain. You are
responsible for understanding your change, running it yourself, and answering
questions about it in review. That is not a rule against AI — being able to
explain your own work is the entire reason you are here.

---

## Rules specific to this project

- **Standard library only.** No new dependencies, not even small ones
- **One file per game** in `arcade/games/`
- **Use `input_utils`**, never bare `input()`
- **Use `art` for colour**, never raw escape codes
- **`play()` returns a number** and must always terminate

---

## Getting unstuck

**Everyone gets stuck. It is not a sign that you do not belong here.**

1. Re-read the issue — the answer is often in "How to verify locally"
2. Read `arcade/games/guess.py`, the simplest game in the project
3. Comment on the issue and tag the mentor listed on it
4. Say what you have already tried — that alone often surfaces the answer
5. Come to a **PR Debug Clinic** (Oct 12, Oct 21) and we will sit with you

### When Git throws something at you

Nine times out of ten it is one of these:

| What you see | What it means |
|---|---|
| `permission denied` on push | You cloned the original, not your fork. Check `git remote -v` |
| `fatal: not a git repository` | You are in the wrong folder. `cd` into the project |
| `Please tell me who you are` | First time using Git. Run the two `git config` lines it prints |
| `Everything up-to-date` but nothing on GitHub | You never committed. Run `git status` |
| `error: failed to push some refs` | Someone changed `main`. `git pull upstream main`, then push again |
| Checks are red on your PR | Click **Details**. It names the file and the line |
| `merge conflict` | Two people edited the same lines. Ask — this one is worth a human |

### Command cheat sheet

```bash
# 1. clone YOUR fork
git clone https://github.com/YOUR-USERNAME/terminal-arcade.git
cd terminal-arcade

# 2. branch
git checkout -b fix/issue-12

# 3. ... make your change in an editor ...

# 4. see what you changed
git status
git diff

# 5. check it works
python3 -m pytest
python3 -m arcade

# 6. commit
git add .
git commit -m "fix: short description of what changed"

# 7. push
git push -u origin fix/issue-12

# then open the pull request, with "Closes #12" in the description
```

Useful when you need to undo something:

```bash
git log --oneline -5             # what did I commit?
git pull upstream main           # get the latest changes
git restore <file>               # throw away uncommitted changes to a file
git switch main                  # go back to the main branch
```

### Where to look things up

| I want to... | Go to |
|---|---|
| Understand a word like "upstream" | [Glossary](https://github-community-gitam.github.io/open-source-launchpad/glossary.html) |
| Check a question others have asked | [FAQ](https://github-community-gitam.github.io/open-source-launchpad/faq.html) |
| Walk through Git again, slowly | [Git basics](https://github-community-gitam.github.io/open-source-launchpad/git-basics.html) |
| Check my PR before I open it | [PR checklist](https://github-community-gitam.github.io/open-source-launchpad/pr-checklist.html) |

---

## Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
In short: be kind, assume good faith, and remember that the person asking a
"basic" question is exactly who this project is for.

---

## Maintainers

| Name | GitHub | Looks after |
|---|---|---|
| Pushpam Raj Satyarthi | [@pushpam2404](https://github.com/pushpam2404) | Everything |

**Domain:** OS & DevX
