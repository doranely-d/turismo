from django import forms

# from linguo.forms import MultilingualModelForm
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['GastronomySectionAdminForm']


class GastronomySectionAdminForm(forms.ModelForm):

    class Meta:
        model = GastronomySection
        exclude = []
        widgets = {
            'sub_title': CKEditorWidget,
            'sub_title_en': CKEditorWidget,
            'sub_title_fr': CKEditorWidget,
            'excerpt': CKEditorWidget,
            'excerpt_en': CKEditorWidget,
            'excerpt_fr': CKEditorWidget,
        }
