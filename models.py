from django.db import models

from allauth import app_settings as allauth_app_settings


class Profile(models.Model):
    user = models.OneToOneField(
        allauth_app_settings.USER_MODEL, on_delete=models.CASCADE)
    crf_patient_pk = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.crf_patient_pk)
