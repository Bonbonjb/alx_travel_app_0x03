from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(to_email, subject, message):
    send_mail(
        subject,
        message,
        'noreply@alxtravel.com',  # Replace with your from address
        [to_email],
        fail_silently=False,
    )
