"""Render the resume to PDF and email it.

Renders the local ``index.html`` (not the live Pages URL) with Chromium's
print emulation, so the ``@media print`` stylesheet is applied and the output
no longer depends on GitHub Pages having already rebuilt. Then emails the PDF.

Credentials are read from environment variables (set as GitHub Actions
secrets): EMAIL_ADDRESS, EMAIL_PASSWORD, RECEIVER_EMAIL.
"""

import os
from pathlib import Path

import yagmail
from playwright.sync_api import sync_playwright

# Resolve paths relative to this file so the script works from any CWD.
REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_HTML = REPO_ROOT / "index.html"
OUTPUT_PDF = Path(__file__).resolve().parent / "cv.pdf"


def render_pdf(source: Path, output: Path) -> None:
    """Render a local HTML file to PDF using headless Chromium."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(source.as_uri(), wait_until="networkidle")
        # Apply the print stylesheet rather than the screen one.
        page.emulate_media(media="print")
        page.pdf(
            path=str(output),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()


def send_email(attachment: Path) -> None:
    """Email the rendered PDF as an attachment."""
    sender_email = os.environ["EMAIL_ADDRESS"]
    sender_password = os.environ["EMAIL_PASSWORD"]
    receiver_email = os.environ["RECEIVER_EMAIL"]

    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=receiver_email,
        subject="Your updated CV in PDF",
        contents="Please find attached your CV in PDF format.",
        attachments=str(attachment),
    )


def main() -> None:
    if not SOURCE_HTML.exists():
        raise FileNotFoundError(f"Resume source not found: {SOURCE_HTML}")
    render_pdf(SOURCE_HTML, OUTPUT_PDF)
    print(f"Rendered PDF: {OUTPUT_PDF}")
    send_email(OUTPUT_PDF)
    print("Email sent successfully!")


if __name__ == "__main__":
    main()
