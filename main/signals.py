from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

@receiver(post_save, sender=Contact)
def send_new_officer_notification_email(sender, instance, created, **kwargs):

    # if a new officer is created, compose and send the email
    if created:
        name = instance.name if instance.name else "no name given"
        subject = instance.subject if instance.subject else "no subject given"
        email = instance.email
        message = instance.message

        print('this is name', name)
        print('this is subject', subject)
        print('this is email', email)
        print('this is message', message)


        send_mail(
            subject,
            "From: " + name + "\nMessage: " + message,
            email,
            ['fadyforextrader@gmail.com'],
            fail_silently=False,
        )