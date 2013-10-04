# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from gallery.models import Photo
from contact.forms import ContactForm, CallMeForm
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        if request.POST['submit'] == 'Enviar mensaje':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                process_valid_contact_form(contact_form)
                return HttpResponseRedirect('/?action=gracias')
            else:
                call_me_form = CallMeForm()
        else:
            call_me_form = CallMeForm(request.POST)
            if call_me_form.is_valid():
                process_valid_call_me_form(call_me_form)
                return HttpResponseRedirect('/?action=gracias')
            else:
                contact_form = ContactForm()
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

def process_valid_contact_form(form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone_number = form.cleaned_data['phone_number']
    message = form.cleaned_data['message']

    send_mail(
        '[reformasbascu.es] Mensaje de ' + name,
        phone_number + '\n\n' + message,
        email,
        ['reformasbascu@gmail.com']
    )

def process_valid_call_me_form(form):
    phone_number = form.cleaned_data['phone_number']

    send_mail(
        '[reformasbascu.es] Llámame',
        phone_number,
        'desconocido@desconocido.com',
        ['reformasbascu@gmail.com']
    )
