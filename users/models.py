import pyotp 

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Blogger(AbstractUser):
    """
    Subclass builtin user model.

    This ensures we can always customise
    our user model if need be.
    """
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'blogger'
        verbose_name_plural = 'bloggers'


@receiver(pre_save, sender=Blogger)
def set_blogger_inactive(sender, instance, **kwargs):
    """Set new bloggers as inactive."""
    instance.is_active = False

@receiver(post_save, sender=Blogger)
def send_activation_code(sender, instance, created, **kwargs):
    """Send a activation code to user email."""
    if created:
        subject = 'Activate Your Yarn Account',
        blogger_id = instance.id
        hotp = pyotp.HOTP('base32secret3232')
        otp = hotp.at(blogger_id)
        message = f"Your Yarn verification code is {otp}."
        from_email = 'no-reply@yarn.com'
        instance.email_user(
            subject=subject, 
            message=message, 
            from_email=from_email
        )


class FollowRelation(models.Model):
    follower = models.ForeignKey(Blogger, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(Blogger, related_name='following', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} followed {self.following}'
