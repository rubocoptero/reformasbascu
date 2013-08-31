import os
from django.conf import settings
from django.db import models
from django.template import defaultfilters
from model_utils.models import TimeStampedModel

# Auxiliary function to determine filename of image uploaded
def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" %(
        defaultfilters.slugify(instance.title),
        extension
    )
    return os.path.join(settings.MEDIA_ROOT, 'photos', filename)

# Model managers

class PhotosManager(models.Manager):
    use_for_related_fields = True

    def carousel(self, **kwargs):
        return self.filter(
            carousel=True, 
            **kwargs)

# App models here.

class Album(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)

class Photo(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    album = models.ForeignKey(Album, blank=True)
    photo = models.ImageField(upload_to=get_file_path)
    carousel = models.BooleanField(default=False)
