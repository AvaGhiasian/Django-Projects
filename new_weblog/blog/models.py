from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse
from django.forms import ModelForm
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


# Create your models here.

# Managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts', verbose_name="نویسنده")

    # data fields
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=200)

    # date
    publish = jmodels.jDateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    # choice fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="وضعیت")
    reading_time = models.PositiveIntegerField(default=0, verbose_name="زمان مطالعه")

    objects = jmodels.jManager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Ticket(models.Model):
    message = models.TextField(verbose_name="پیام")
    name = models.CharField(max_length=250, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    subject = models.CharField(max_length=100, verbose_name="موضوع")

    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Comment(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    body = models.TextField(verbose_name="متن کامنت")
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    active = models.BooleanField(default=False, verbose_name="وضعیت")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="پست")

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return f"{self.name}: {self.post}"


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images", verbose_name="پست")
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    created = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ انتشار")
    image_file = ResizedImageField(upload_to="post_images/", size=[500, 500], quality=75, crop=['middle', 'center'])

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویرها"

    def __str__(self):
        return self.title
