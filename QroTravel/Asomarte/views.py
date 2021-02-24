from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.http import Http404

from .models import *


def landing(request):
    configuration = Configuration.objects.get()
    videos = Video.objects.all()[:6]
    return TemplateResponse(request, 'asomarte/asomarte.html', locals())
