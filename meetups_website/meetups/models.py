from django.db import models

# Create your models here.


class Meetup(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.title} - {self.location}"
