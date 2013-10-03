from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from gallery.models import Photo
from contact.forms import ContactForm, CallMeForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
    else:
        contact_form = ContactForm()
        call_me_form = CallMeForm()

    carousel_list = Photo.objects.carousel()
    albums = Photo.objects.gallery_by_album()

    return render_to_response(
        "index.html", 
        locals(), 
        context_instance=RequestContext(request),
    )

