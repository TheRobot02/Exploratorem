import smtplib
import base64
class send_mail:
    def __init__(self):
        
        # zet de gegevens voor de e-mail
        self.FROM_EMAIL = "klooien90@hotmail.com"
        self.TO_EMAIL = "infranaat3@gmail.com"
        self.PASSWORD = "s3samzaad"
        self.HOST = "smtp-mail.outlook.com"
        self.PORT = 587
        self.BESTAND = "test.txt"

    def mailSend(self):
        # maak de SMTP-verbinding
        smtp_server = smtplib.SMTP(self.HOST, self.PORT)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(self.FROM_EMAIL, self.PASSWORD)

        # lees het bestand in als bytes
        with open(self.BESTAND, "rb") as f:
            file_data = f.read()

        # converteer de bytes naar base64
        file_data_b64 = base64.b64encode(file_data).decode()

        # maak de MIME-headers
        subject = "Get Huge Co-w, NOW!"
        boundary = "===my_boundary==="
        attachment_filename = self.BESTAND
        headers = f"""From: {self.FROM_EMAIL}
        To: {self.TO_EMAIL}
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

        smtp = smtplib.SMTP(self.HOST, self.PORT)

        status_code, response = smtp.ehlo()
        print(f"[*] Echoing the server: {status_code} {response}")

        status_code, response = smtp.starttls()
        print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(self.FROM_EMAIL, self.PASSWORD)
        print(f"[*] Logging in: {status_code} {response}")

        # verstuur de e-mail
        smtp_server.sendmail(self.FROM_EMAIL, self.TO_EMAIL, headers)

        # verbreek de SMTP-verbinding
        smtp_server.quit()

if __name__ == "__main__":
    mail = send_mail()
    mail.mailSend()