from django.core.mail import send_mail
from django.conf import settings


def sent_forget_password_mail(email, token):
    subject = 'your forget password link'
    message =  f'hii , Click Here to change Password http://127.0.0.1:8000/changepassword/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)
    return True
