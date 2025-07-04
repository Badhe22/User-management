
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_disabled = models.BooleanField(default=False)
    
    def is_active_for_authentication(self):
        return super().is_active and not self.is_disabled