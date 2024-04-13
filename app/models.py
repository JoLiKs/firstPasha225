from django.db import models

# Create your models here.
from django.db import models


class Users(models.Model):
    name = models.TextField()
    email = models.TextField()
    login = models.TextField()
    password = models.TextField()