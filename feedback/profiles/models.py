from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # files should be stored in the hard instead of DB bcs they make DB slow
    # .FileField() stores files in the hard and only stores the path in the DB
    image = models.ImageField()