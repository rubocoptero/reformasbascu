from django.shortcuts import render_to_response
from gallery.models import Photo

def home(request):
    carousel_list = Photo.objects.carousel()
    albums = Photo.objects.gallery_by_album()
    return render_to_response("index.html", locals())
