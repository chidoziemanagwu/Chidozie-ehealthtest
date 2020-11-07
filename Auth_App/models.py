from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


HealthUserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        HealthUserModel,
        max_length=300,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='client',  # related name manager if needed
        null=False,
        blank=False,
    )

    userphonenumber = models.CharField(
        help_text='Your phone number',
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )
    
    medical_practitioner = models.BooleanField(
        null=False,
    )

    job_title = models.CharField(
        help_text='Your job description',
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}, user profile.'.format(self.user.username)
