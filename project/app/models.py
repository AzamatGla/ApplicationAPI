from django.contrib.auth.models import User
from django.db import models
import random
import string

class Application(models.Model):
    name = models.CharField(max_length=250)
    api_key = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='applications', blank=True) #для возможности одному пользователю создавать несколько приложений

    def __str__(self):
        return self.name

    def generate_key(length=128):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

