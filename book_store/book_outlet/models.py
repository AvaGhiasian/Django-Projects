from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify  # imports the built in slugify helper

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.postal_code}, {self.street}, {self.city}"

    # meta configurations for addr model
    class Meta:
        # how the addr model should be output specially when plural is needed
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    # no rating should be higher than 5 and less than 1, so validators are needed
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    # null=True allows that a book author can be null
    # related_names: used for reverse of the relation
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_best_selling = models.BooleanField(default=False)

    # if book name is Harry Potter auto populate to harry-potter
    # db_index: a technical detail, DB will save the value in a way that makes searching them a bit more efficient.
    # so creating a field like this db_index=True makes searching the field quicker.
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, unique=True)

    # many to many relation is set up differently behind the scene.
    # in one to many or one to one, 2 tables are involved & info is stored in one of the tables.
    # for many to many rel, django automatically creates a 3rd table.
    # the tables holds one row per connection between country and book.
    # so if a book belongs to 2 countries, 2 rows would be added in between the table.
    published_countries = models.ManyToManyField(Country, related_name="books")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"title: {self.title}, rate: {self.rating}"
