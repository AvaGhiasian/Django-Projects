from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")

    def __str__(self):
        return self.title


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.user_name} - {self.watchlist.title} | {self.rating}"
