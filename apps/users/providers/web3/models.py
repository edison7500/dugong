from django.db import models
from django.conf import settings


USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class WalletAccount(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=256)
    extra_data = models.JSONField(default={})

    def __str__(self):
        return self.public_key
