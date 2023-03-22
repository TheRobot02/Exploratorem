import smtplib
import base64

# zet de gegevens voor de e-mail
FROM_EMAIL = "klooien90@hotmail.com"
TO_EMAIL = "infranaat3@gmail.com"
PASSWORD = "s3samzaad"
HOST = "smtp-mail.outlook.com"
PORT = 587
BESTAND = "test.txt"
# maak de SMTP-verbinding
smtp_server = smtplib.SMTP(HOST, PORT)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login(FROM_EMAIL, PASSWORD)

# lees het bestand in als bytes
with open(BESTAND, "rb") as f:
    file_data = f.read()

# converteer de bytes naar base64
file_data_b64 = base64.b64encode(file_data).decode()

# maak de MIME-headers
subject = "Get Huge Co-w, NOW!"
boundary = "===my_boundary==="
attachment_filename = BESTAND
headers = f"""From: {FROM_EMAIL}
To: {TO_EMAIL}
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Are you ready?

--{boundary}
Content-Type: application/pdf; name="{attachment_filename}"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="{attachment_filename}"

{file_data_b64}

--{boundary}--"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

# verstuur de e-mail
smtp_server.sendmail(FROM_EMAIL, TO_EMAIL, headers)

# verbreek de SMTP-verbinding
smtp_server.quit()