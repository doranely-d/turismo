from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from .models import *
from Blog.models import Post


def landing(request):
    configuration = Configuration.objects.get()
    qs = Region.objects.all()
    qs_post = Post.objects.select_related('category').all().order_by('?')[:3]
    return TemplateResponse(request, 'regions/regions_landing.html', locals())


def region(request, region_id, slug=None):
    region = get_object_or_404(
        Region.objects.prefetch_related('sections'),
        pk=region_id
    )
    qs = region.sections.all()
    qs_post = Post.objects.select_related('category').all().order_by('?')[:3]
    return TemplateResponse(request, 'regions/region.html', locals())


def section(request, section_id, slug=None):
    section = get_object_or_404(
        Section.objects.prefetch_related('region'),
        pk=section_id
    )
    return TemplateResponse(request, 'regions/section.html', locals())
