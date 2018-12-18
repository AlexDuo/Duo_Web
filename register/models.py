from django.db import models

# Create your models here.

class user_info_entity(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

# after we create the data entity we need to map this stuff to real sql through python manage.py makemigrations
# an python manage.py migrate