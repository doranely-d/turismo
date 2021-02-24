from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['FeedAdminForm']


class FeedAdminForm(forms.ModelForm):

    class Meta:
        model = Feed
        exclude = []
        widgets = {
            'content': CKEditorWidget,
        }
