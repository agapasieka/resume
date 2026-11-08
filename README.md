# resume

My CV as a small static site — plain HTML and CSS, no build step — hosted on
GitHub Pages.

**Live:** https://agapasieka.github.io/resume/

[![CodeQL](https://github.com/agapasieka/resume/actions/workflows/codeql.yml/badge.svg)](https://github.com/agapasieka/resume/actions/workflows/codeql.yml)
[![Scorecard supply-chain security](https://github.com/agapasieka/resume/actions/workflows/scorecard.yml/badge.svg)](https://github.com/agapasieka/resume/actions/workflows/scorecard.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/agapasieka/resume/badge)](https://securityscorecards.dev/viewer/?uri=github.com/agapasieka/resume)

## How it's hosted

- `index.html` + `style.css`, served by GitHub Pages straight from `main`.
- The page adapts to light/dark mode, and a print stylesheet means it renders
  to a clean, ATS-friendly PDF.

## Workflows

| Workflow | Trigger | What it does |
| --- | --- | --- |
| **PDF + email** (`html-pdf-workflow.yml`) | Manual (Actions → *Run workflow*) | Renders the local `index.html` to a PDF with Playwright and emails it. See [`html-pdf-converter/`](html-pdf-converter/README.md). |
| **CodeQL** (`codeql.yml`) | Push / PR / weekly | Static code-scanning. |
| **Scorecard** (`scorecard.yml`) | Push / weekly | OpenSSF supply-chain security scoring. |
| **gitleaks** (`gitleaks.yml`) | Push / PR | Secret scanning (defense-in-depth). |
| **Dependabot auto-merge** (`dependabot-auto-merge.yml`) | Dependabot PRs | Auto-merges vetted dependency bumps. |

Dependencies are kept current by **Dependabot** and **Renovate**, and all
GitHub Actions are pinned to full commit SHAs. Security issues: see
[`SECURITY.md`](SECURITY.md).

## Layout

```
index.html              # the resume
style.css               # styling (light/dark + print)
html-pdf-converter/     # Playwright script that renders + emails the PDF
.github/workflows/      # PDF/email + security workflows
SECURITY.md             # vulnerability reporting policy
```
