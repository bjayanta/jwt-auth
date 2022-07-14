import random
from turtle import ht
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

User = get_user_model()

def send_otp_via_email(email):
    subject = 'Your account verification email'
    otp = random.randint(1000, 9999)
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST

    # send email
    send_mail(subject, message, email_from, [email], ht)

    # save the otp
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()

def send_otp_via_email_template(email):
    # get user
    user = User.objects.get(email = email)

    subject = 'Your account verification email'
    otp = random.randint(1000, 9999)
    message = f'Your OTP is {otp}'
    email_from = settings.DEFAULT_FROM_EMAIL

    # setup email template
    html = render_to_string('account/email_template.html', {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': email,
        'content': message
    })

    # send email
    send_mail(subject, message, email_from, [email], html_message=html)

    # save the otp
    user.otp = otp
    user.save()
