# Render the resume to PDF and email it

A small GitHub Actions job that renders the resume to a PDF and emails it as an
attachment. It is triggered manually from the **Actions** tab ("Run workflow"),
so a PDF is only sent when you ask for one.

## How it works

1. **Install dependencies** — `playwright` (headless Chromium) for rendering and
   `yagmail` for sending the email, from `requirements.txt`.
2. **Install the browser** — `playwright install --with-deps chromium`.
3. **Render + send** — `html-pdf-converter-email.py`:
   * Opens the local `index.html` in headless Chromium.
   * Switches to print media so the `@media print` rules in `style.css` apply,
     then saves `cv.pdf` (A4).
   * Emails `cv.pdf` with `yagmail`.

Rendering the **local** file (rather than the live
`https://agapasieka.github.io/resume/` URL) means the PDF reflects the exact
commit being run and does not depend on GitHub Pages having already rebuilt.

## Secrets

Set these as repository secrets (Settings → Secrets and variables → Actions):

| Secret           | Purpose                                                        |
| ---------------- | ------------------------------------------------------------- |
| `EMAIL_ADDRESS`  | Sender address.                                               |
| `EMAIL_PASSWORD` | Sender password / app password (Gmail with 2FA → App Password).|
| `RECEIVER_EMAIL` | Recipient address.                                            |

## Running locally

```bash
cd html-pdf-converter
pip install -r requirements.txt
python3 -m playwright install chromium
EMAIL_ADDRESS=... EMAIL_PASSWORD=... RECEIVER_EMAIL=... python3 html-pdf-converter-email.py
```
