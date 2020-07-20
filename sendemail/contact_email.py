from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage

class AutoMail(object):
    @staticmethod
    def contact_us(email_list, email_content, lead_email):
        try:
            msg = MIMEMultipart('related')
            msg['Subject'] = "This email is from Boom Ecommerce"
            msg['From'] = 'boomentrepreneurship@gmail.com'
            msg['To'] = 'boomentrepreneurship@gmail.com'
            email_content = 'Trials!'
            email = EmailMessage("Hi! I like your website", email_content, to='', cc=[lead_email])
            email.send()
            return True
        except:
            raise