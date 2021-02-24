from django import forms

# from linguo.forms import 
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['RegionAdminForm', 'SectionAdminForm']


class RegionAdminForm(forms.ModelForm):

    class Meta:
        model = Region
        exclude = []
        widgets = {
            'sub_title': CKEditorWidget,
            'sub_title_en': CKEditorWidget,
            'sub_title_fr': CKEditorWidget,
            'heading': CKEditorWidget,
            'heading_en': CKEditorWidget,
            'heading_fr': CKEditorWidget,
            'sub_heading': CKEditorWidget,
            'sub_heading_en': CKEditorWidget,
            'sub_heading_fr': CKEditorWidget,
            'extra_data': CKEditorWidget,
            'extra_data_en': CKEditorWidget,
            'extra_data_fr': CKEditorWidget,
        }


class SectionAdminForm(forms.ModelForm):

    class Meta:
        model = Section
        exclude = []
        widgets = {
            'content': CKEditorWidget,
            'content_en': CKEditorWidget,
            'content_fr': CKEditorWidget,
            'sub_title': CKEditorWidget,
            'sub_title_en': CKEditorWidget,
            'sub_title_fr': CKEditorWidget,
            'sub_heading': CKEditorWidget,
            'sub_heading_en': CKEditorWidget,
            'sub_heading_fr': CKEditorWidget,
        }
