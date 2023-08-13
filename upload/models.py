from django.db import models
import io
import PIL
from PIL import Image
from django.utils.text import slugify

# Create your models here.

# path of image location on server


def image_location(instance, filename, **kwargs):
    file_path = f"image/{instance.title}-{filename}"
    return file_path

# path of pdf location on server


def pdf_location(instance, filename, **kwargs):
    file_path = f"pdf/{instance.title}-{filename}"
    return file_path


class ImageModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=image_location, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    def __str__(self):
        return self.title


class PdfModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)
    pdf = models.FileField(upload_to=pdf_location, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    def __str__(self):
        return self.title
