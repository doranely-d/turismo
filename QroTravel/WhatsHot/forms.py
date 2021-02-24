# -*- coding: utf-8 -*-
from django import forms

from .models import *


__all__ = ['CategoryOptionsFilterForm']


class CategoryOptionsFilterForm(forms.Form):

    def __init__(self, category, *args, **kwargs):
        super(CategoryOptionsFilterForm, self).__init__(*args, **kwargs)
        for cf in category.filters.all():
            self.fields['cf_%d' % cf.id] = forms.ModelMultipleChoiceField(
                label=cf.name, queryset=cf.options.all(), required=False,
                widget=forms.CheckboxSelectMultiple,
            )
