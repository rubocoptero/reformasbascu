import os
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from model_utils.models import TimeStampedModel
from .managers import PhotosManager

# Auxiliary function to determine filename of image uploaded
def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" %(
        slugify(instance.title),
        extension
    )
    return os.path.join('photos', filename)


class Album(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.title

class Photo(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    album = models.ForeignKey(Album, blank=True, null=True, default=None)
    photo = models.ImageField(upload_to=get_file_path)
    carousel = models.BooleanField(default=False)
    objects = PhotosManager()

    def __unicode__(self):
        return self.title
