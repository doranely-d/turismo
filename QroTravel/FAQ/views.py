from django.utils.translation import ugettext_lazy as _

from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import Http404

from .models import *


def landing(request):
    category = Category.objects.exclude(questions=None).first()
    if category:
        return redirect(category.absolute_url())
    raise Http404


def faq_category(request, category_id, slug=None):
    title = (_('FAQs'))
    configuration = Configuration.objects.get()
    instance = get_object_or_404(
        Category.objects.prefetch_related('questions'),
        pk=category_id,
    )
    categories = Category.objects.exclude(questions=None)
    return TemplateResponse(request, 'FAQ/faqs.html', locals())
