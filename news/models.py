from django.db import models
from helpers.models import BaseModel


# Create your models here.

# CATEGORY:
class Category(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


# TAG:
class Tag(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


# REGION:
class Region(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


# NEWS:
class News(BaseModel):
    title = models.CharField(max_length=128, verbose_name='Title')
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sub_content = models.CharField(max_length=256)
    image = models.ImageField(upload_to="news/", null=True, blank=True)
    image_caption = models.CharField(max_length=128, null=True, blank=True)
    published_datetime = models.DateTimeField(null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='news', blank=True)
    tags = models.ManyToManyField(Tag, related_name='news', null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    is_main = models.BooleanField(default=False)
    is_editor_choice = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_investigation = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)
    is_videonews = models.BooleanField(default=False)
    is_photonews = models.BooleanField(default=False)
    is_adviced = models.BooleanField(default=False)

    def __str__(self):
        return self.title
