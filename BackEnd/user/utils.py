from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user):
    subject = 'Confirm your email'
    message = f'Hola {user.first_name}, please confirm your email by clicking the following link: http://example.com/confirm/{user.email}/{user.confirmation_token}/'
    recipient_list = [user.email]
    from_email = settings.DEFAULT_FROM_EMAIL
    
    send_mail(subject, message, from_email, recipient_list)