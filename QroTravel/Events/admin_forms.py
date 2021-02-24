from django import forms

# from linguo.forms import MultilingualModelForm
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['EventAdminForm']


class EventAdminForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = []
        widgets = {
            'content': CKEditorWidget,
            'content_en': CKEditorWidget,
            'content_fr': CKEditorWidget,
            'address': CKEditorWidget,
        }
