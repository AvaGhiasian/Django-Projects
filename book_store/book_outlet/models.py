from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify # this imports the built in slugify helper

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    # no rating should be higher than 5 and less than 1, so validators are needed
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MinValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False) # if book name is Harry Potter auto populate to harry-potter

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    def save(self, *args, **kwargs):
        """
        title is taken and sat to slug filed, so this transforms the title into a slug,
        then super().save() is called to save the data to the DB.
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"title: {self.title}, rate: {self.rating}"
