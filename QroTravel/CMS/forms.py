from django.utils.translation import ugettext_lazy as _
from django import forms

from CMS.models import Contact
from lib.email import send_mail

__all__ = ['ContactForm']


class ContactForm(forms.Form):
    name = forms.CharField(label=_('name'))
    email = forms.EmailField(label=_('email'))
    subject = forms.CharField(label=_('subject'))
    message = forms.CharField(label=_('message'), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, *args, **kwargs):
        contact = Contact.objects.get()
        data = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        send_mail('contact', [contact.contact_email], context=data)
