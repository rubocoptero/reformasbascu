# -*- coding: utf-8 -*-

from django import forms
from django.contrib.localflavor.es.forms import ESPhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from crispy_forms.bootstrap import FieldWithButtons, FormActions

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Nombre:',
    )
    email = forms.EmailField(
        label='Correo electrónico:',
    )
    phone_number = ESPhoneNumberField(
        label='Número de teléfono:',
        required = False,
    )
    message = forms.CharField(
        widget = forms.Textarea(),
        label='Mensaje:',
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contactForm'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = '/#contacto'

        self.helper.layout = Layout(
            Div(
                Field('name', wrapper_class='span2', css_class='span2'),
                Field('email', wrapper_class='span2', css_class='span2'),
                Field(
                    'phone_number',
                    wrapper_class='span2', 
                    css_class='span2',
                    placeholder='Opcional',
                ),
                css_class='controls-row',
            ),
            Div(
                Div(
                    Field('message', css_class='span6'), 
                    css_class='span6'
                ), 
                css_class='controls-row',
            ),
            FormActions(
                Div(
                    Submit(
                        'submit', 
                        'Enviar mensaje', 
                        css_class='btn-inverse', 
                        style='margin-right: 1em;',
                    ),
                    css_class='control-group span6'
                ),
                css_class='form-actions text-right',
            ),
        )

        self.helper.html5_required = True

class CallMeForm(forms.Form):
    phone_number = ESPhoneNumberField(
        label='Introduzca su número de teléfono:',
    )

    def __init__(self, *args, **kwargs):
        super(CallMeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-callMeForm'
        self.helper.form_class = 'form-inline text-left'
        self.helper.form_method = 'post'
        self.helper.form_action = '/#contacto'

        self.helper.layout = Layout(
            FieldWithButtons('phone_number', 
                Submit(
                    'submit',
                    'Llámenme'.decode('utf-8'), 
                    css_class='btn-inverse'
                )
            ),
        )

        self.helper.html5_required = True

