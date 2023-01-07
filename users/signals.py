from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models import Profile


# Create profile automatically for newly registered user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

        subject = "Welcome to Dev2Cents"
        body = "You have signed up to Dev2Cents, we are glad you are here. Make Cents, motivate others, talk about " \
               "tech and keep things fun "

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[profile.email],
            reply_to=None,
            headers={'Content-Type': 'text/plain'},
        )
        email.send(fail_silently=False)


# function to update user information if profile is updated
@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()


# delete user account if profile is deleted
@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
