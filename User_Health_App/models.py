from django.db import models
from django.contrib.auth import get_user_model

HealthUserModel = get_user_model()


class UserHealthInfo(models.Model):
    user = models.ForeignKey(
        HealthUserModel,
        max_length=300,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='client_health',  # related name manager if needed
        null=False,
        blank=False,
    )

    Gender = models.CharField(
        max_length=10,
        null=False,
    )

    age = models.CharField(
        max_length=2,
        null=False,
    )

    blood_group = models.CharField(
        max_length=100,
        null=False,
    )

    genotype = models.CharField(
        max_length=100,
        null=False,
    )

    ebola_status = models.BooleanField(
        help_text='Do you have ebola currently?',
        blank=False,
        null=False,
    )

    malaria_status = models.BooleanField(
        help_text='Do you have malaria currently?',
        null=False,
    )

    previous = models.BooleanField(
        help_text='Do you have previous health challenges?',
        null=False,
    )

    previous_illness1 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    previous_illness2 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    previous_illness3 = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    previous_illness4 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    previous_illness5 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}, Health info.'.format(self.user.username)
