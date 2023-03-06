from django.db import models


class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=5000)

