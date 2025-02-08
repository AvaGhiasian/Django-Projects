from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    # no rating should be higher than 5 and less than 1, so validators are needed
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MinValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"title: {self.title}, rate: {self.rating}"
