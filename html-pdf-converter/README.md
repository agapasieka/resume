# Run workflow and email the file converted to pdf 
This approach leverages 'yagmail' to simplify the process of sending emails with attachments, making it easier to integrate email functionality into GitHub Actions workflow.

<!-- Overview -->
# Explanation

1. Install dependencies:

  * Installs pyhtml2pdf for converting HTML to PDF and yagmail for sending emails with attachments.

2. Convert HTML to PDF and Send Email:

  * Runs a Python script inline to:
    * Convert a html resume or any webpage (https://example.com/resume) to a PDF and save it as cv.pdf.
    * Use yagmail to send an email with cv.pdf as an attachment.

3. Email Settings:

  * sender_email: The sender's email address (stored in the EMAIL_ADDRESS secret).
  * sender_password: The sender's password (stored in the EMAIL_PASSWORD secret).
  * receiver_email: The recipient's email address (stored in the RECEIVER_EMAIL).
  * subject: The email subject line.
  * body: The email body content.

4. Secrets:

  * EMAIL_ADDRESS, EMAIL_PASSWORD and RECEIVER_EMAIL are secrets stored in your GitHub repository. The EMAIL_PASSWORD can be an App Password if you're using Gmail with 2-Step Verification enabled.

<!-- Task -->
# Adding the Secrets to GitHub

1. Go to your repository on GitHub.
2. Click on Settings.
3. In the left sidebar, click on Secrets and variables > Actions.
4. Click New repository secret.
5. Add the EMAIL_ADDRESS, EMAIL_PASSWORD and RECEIVER_EMAIL secrets with the appropriate values.

<!-- Task -->
# Using the Workflow

When you merge your branch(PR) to main, workflow will automatically trigger, performing the following:

  * Convert the specified webpage into a PDF.
  * Send an email with the generated PDF (cv.pdf) attached to the specified recipient.





