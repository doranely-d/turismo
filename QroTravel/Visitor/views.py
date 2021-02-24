from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from .models import *
from Blog.models import Post
from CMS.models import Contact


def landing(request):
    configuration = QueretaroLanding.objects.get()
    qs = QueretaroSection.objects.all()
    qs_post = Post.objects.select_related('category').all().order_by('?')[:3]
    return TemplateResponse(request, 'visitors/queretaro_landing.html', locals())


def visitors_guide(request):
    configuration = Configuration.objects.get()
    contact = Contact.objects.get()
    qs_season = Season.objects.all()
    qs_section = Section.objects.all()
    qs_transportation = TransportationType.objects.all()
    return TemplateResponse(request, 'visitors/visitors_guide.html', locals())
