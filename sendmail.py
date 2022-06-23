import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SendEmail(html):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "EXPENSE SUMMARY"
    msg["From"] = 'galvaradotest@gmail.com'
    msg["To"] = 'geovanny.alvaradod@gmail.com'
    filename = "movimientos.csv"


 

    part = MIMEText(html, "html")

    msg.attach(part)

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        "attachment", filename= filename
    )
    msg.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('galvaradotest@gmail.com', 'qevrpvrumgovhauj')
        server.sendmail(
            'galvaradotest@gmail.com', 'geovanny.alvaradod@gmail.com', msg.as_string()
        )