from django.db import models

# Create your models here.
from django.db import models


class users(models.Model):
    email = models.TextField()
    login = models.TextField()
    password = models.TextField()