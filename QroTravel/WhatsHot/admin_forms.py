# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

# from linguo.forms import forms.ModelForm
from ckeditor.widgets import CKEditorWidget

from .models import *


__all__ = ['CardAdminForm', 'SectionAdminForm']


class CardAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardAdminForm, self).__init__(*args, **kwargs)
        category = None
        self.fields['category'].required = True
        if self.instance.category_id:
            category = self.instance.category
        else:
            category_id = self.data.get('category', None)
            if category_id:
                try:
                    category = Category.objects.get(pk=category_id)
                except:
                    pass
        if category and not category.has_sections:
            for cf in category.filters.all():
                cfo = cf.options.all()
                try:
                    selected = self.instance.category_filters.filter(id__in=cfo.values_list('id', flat=True)).first()
                except:
                    selected = None
                self.fields['category_filter_option_%d' % cf.id] = forms.ModelChoiceField(
                    label=cf.name, queryset=cfo, initial=selected, required=False
                )
        else:
            self.fields['category'].help_text = 'Selecciona una categoría y da click en guardar para que aprezcan los demás campos'

    def _save_m2m(self):
        super(CardAdminForm, self)._save_m2m()
        if self.category_filters:
            self.instance.category_filters = self.category_filters

    def save(self, commit=True):
        cfo_arr = []
        category = self.instance.category
        for cf in category.filters.all():
            cfo = self.cleaned_data.get('category_filter_option_%d' % cf.id, None)
            if cfo:
                cfo_arr.append(cfo)
        if commit:
            self.instance.save()
            self.category_filters = cfo_arr
            self._save_m2m()
        else:
            self.category_filters = cfo_arr
            self.save_m2m = self._save_m2m
        return self.instance

    class Meta:
        model = Card
        exclude = []
        widgets = {
            'description': CKEditorWidget,
            'description_en': CKEditorWidget,
            'description_fr': CKEditorWidget,
            'subtitle': CKEditorWidget,
            'subtitle_en': CKEditorWidget,
            'subtitle_fr': CKEditorWidget,
        }


class SectionAdminForm(forms.ModelForm):
    main_category = forms.ModelChoiceField(
        queryset=Category.objects.filter(has_sections=True),
        label=_('main category')
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.filter(has_sections=True),
        label=_('other categories'), required=False
    )

    def __init__(self, *args, **kwargs):
        super(SectionAdminForm, self).__init__(*args, **kwargs)
        main_category = None
        self.fields['main_category'].required = True
        if self.instance.main_category_id:
            main_category = self.instance.main_category
        else:
            main_category_id = self.data.get('main_category', None)
            if main_category_id:
                try:
                    main_category = Category.objects.get(pk=main_category_id)
                except:
                    pass
        if main_category and main_category.has_sections:
            self.fields['categories'].queryset = Category.objects.filter(has_sections=True).exclude(id=main_category.id)
            for cf in main_category.filters.all():
                cfo = cf.options.all()
                try:
                    selected = self.instance.category_filters.filter(id__in=cfo.values_list('id', flat=True)).first()
                except:
                    selected = None
                self.fields['category_filter_option_%d' % cf.id] = forms.ModelChoiceField(
                    label=cf.name, queryset=cfo, initial=selected, required=False
                )
        else:
            self.fields['main_category'].help_text = 'Selecciona una categoría y da click en guardar para que aprezcan los demás campos'

    def _save_m2m(self):
        super(SectionAdminForm, self)._save_m2m()
        if self.category_filters:
            self.instance.category_filters = self.category_filters

    def save(self, commit=True):
        cfo_arr = []
        main_category = self.instance.main_category
        for cf in main_category.filters.all():
            cfo = self.cleaned_data.get('category_filter_option_%d' % cf.id, None)
            if cfo:
                cfo_arr.append(cfo)
        if commit:
            self.instance.save()
            self.category_filters = cfo_arr
            self._save_m2m()
        else:
            self.category_filters = cfo_arr
            self.save_m2m = self._save_m2m
        return self.instance

    class Meta:
        model = Section
        exclude = []
