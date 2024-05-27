from Model.TemporaryUserModel import TemporaryUserModel

class TemporaryUserController:
    @staticmethod
    def CreateTemporaryUser(republic_of_turkey_id_card_no, patient_id, patient_email):
        password = TemporaryUserModel.CreateTemporaryUser(republic_of_turkey_id_card_no, patient_id)
        TemporaryUserController.send_email(patient_email, password)
        return password

    @staticmethod
    def AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password):
        return TemporaryUserModel.AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password)

    @staticmethod
    def send_email(to_email, password):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import smtplib
        import os

        EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
        EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

        subject = 'Temporary User Created for Your Test'
        body = f'A temporary user has been created for your test.\n\nTemporary Password: {password}'

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
