from django import forms

# from linguo.forms import MultilingualModelForm
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['PostAdminForm']


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = []
        widgets = {
            'content': CKEditorWidget,
            'content_en': CKEditorWidget,
            'content_fr': CKEditorWidget,
        }
