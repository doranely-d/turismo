from django import forms

# from linguo.forms import MultilingualModelForm
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['ConfigurationAdminForm', 'SectionAdminForm', 'QueretaroSectionAdminForm', 'QueretaroLandingAdminForm']


class ConfigurationAdminForm(forms.ModelForm):

    class Meta:
        model = Configuration
        exclude = []
        widgets = {
            'sub_heading': CKEditorWidget,
            'sub_heading_en': CKEditorWidget,
            'sub_heading_fr': CKEditorWidget,
        }


class SectionAdminForm(forms.ModelForm):

    class Meta:
        model = Section
        exclude = []
        widgets = {
            'sub_heading': CKEditorWidget,
            'sub_heading_en': CKEditorWidget,
            'sub_heading_fr': CKEditorWidget,
        }


class QueretaroSectionAdminForm(forms.ModelForm):

    class Meta:
        model = QueretaroSection
        exclude = []
        widgets = {
            'sub_title': CKEditorWidget,
            'sub_title_en': CKEditorWidget,
            'sub_title_fr': CKEditorWidget,
            'excerpt': CKEditorWidget,
            'excerpt_en': CKEditorWidget,
            'excerpt_fr': CKEditorWidget,
        }


class QueretaroLandingAdminForm(forms.ModelForm):

    class Meta:
        model = QueretaroLanding
        exclude = []
        widgets = {
            'faqs_text': CKEditorWidget,
            'faqs_text_en': CKEditorWidget,
            'faqs_text_fr': CKEditorWidget,
        }
