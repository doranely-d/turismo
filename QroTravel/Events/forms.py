# -*- coding: utf-8 -*-
from django import forms

from .models import *


__all__ = ['CalendarFilterForm']


class CalendarFilterForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        label='', required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.none(),
    )

    def __init__(self, events, *args, **kwargs):
        super(CalendarFilterForm, self).__init__(*args, **kwargs)
        cat_ids = events.values_list('category__id', flat=True)
        if cat_ids:
            self.fields['category'].queryset = Category.objects.filter(id__in=cat_ids)
            self.fields['category'].filter_field = 'category'
        else:
            del(self.fields['category'])
