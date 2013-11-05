# -*- coding: utf-8 -*-

from django import forms
from localflavor.es.forms import ESPhoneNumberField
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
        self.helper.form_class = 'form-inline span11'
        self.helper.form_method = 'post'
        self.helper.form_action = '/#contacto'

        self.helper.layout = Layout(
            Div(
                Field('name', wrapper_class='span4', css_class='span12'),
                Field('email', wrapper_class='span4', css_class='span12'),
                Field(
                    'phone_number',
                    wrapper_class='span4', 
                    css_class='span12',
                    placeholder='Opcional',
                ),
                css_class='controls-row',
            ),
            Div(
                Field('message', css_class='input-block-level'), 
                css_class='control-row'
            ),
            FormActions(
                Div(
                    Submit(
                        'submit', 
                        'Enviar mensaje', 
                        css_class='btn-inverse',
                    ),
                    css_class='control-group span12'
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

