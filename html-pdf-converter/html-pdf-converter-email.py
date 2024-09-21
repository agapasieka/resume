# Import Required Libraries
import os
import yagmail
from pyhtml2pdf import converter

# Convert HTML to PDF
converter.convert('https://agapasieka.github.io/resume/', 'cv.pdf')     # Replace the web page link and pdf file name  

# Email settings
sender_email = os.getenv('EMAIL_ADDRESS')
sender_password = os.getenv('EMAIL_PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL') 
subject = 'Your updated CV in PDF'
body = 'Please find attached your CV in PDF format.'

# Send the email with the attachment
yag = yagmail.SMTP(sender_email, sender_password)
yag.send(
    to=receiver_email,
    subject=subject,
    contents=body,
    attachments='cv.pdf'
)

print("Email sent successfully!")