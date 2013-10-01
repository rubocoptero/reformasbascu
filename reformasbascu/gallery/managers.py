from collections import defaultdict
from django.db import models

class PhotosManager(models.Manager):
    use_for_related_fields = True

    def carousel(self, **kwargs):
        return self.filter(
            carousel=True, 
            **kwargs)

    def gallery_by_album(self, **kwargs):
        photos_in_albums = self.filter(album__isnull=False, **kwargs) \
            .select_related()
        photos_by_album = defaultdict(list)
        for photo in photos_in_albums:
            photos_by_album[photo.album.title].append(photo)

        return dict(photos_by_album)


