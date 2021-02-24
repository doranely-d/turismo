from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from .models import *
from Blog.models import Post


def landing(request):
    configuration = GastronomyLanding.objects.get()
    qs = GastronomySection.objects.all()
    qs_post = Post.objects.select_related('category').all().order_by('?')[:3]
    return TemplateResponse(request, 'gastronomy/landing.html', locals())
