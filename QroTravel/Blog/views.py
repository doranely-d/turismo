from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.conf import settings
from django.http import Http404

from datetime import datetime, date

from CMS.models import Inspiration
from .models import *

PAGINATOR_ITEMS = getattr(settings, 'PAGINATOR_ITEMS', 9)


def categories(request):
    configuration = Configuration.objects.get()
    categories = Category.objects.all()
    qs = Post.objects.filter(featured=True)[:3]
    paginator = Paginator(qs, PAGINATOR_ITEMS)
    page = request.GET.get('page')
    try:
        list_items = paginator.page(page)
        page = int(page)
    except PageNotAnInteger:
        page = 1
        list_items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        list_items = paginator.page(page)
    if request.is_ajax():
        return TemplateResponse(request, 'blog/ajax_category.html', locals())
    return TemplateResponse(request, 'blog/categories.html', locals())


def category(request, category_id, slug=None):
    configuration = Configuration.objects.get()
    category = get_object_or_404(
        Category.objects.prefetch_related('posts'), pk=category_id
    )
    posts = category.posts.all()
    paginator = Paginator(posts, PAGINATOR_ITEMS)
    page = request.GET.get('page')
    try:
        list_items = paginator.page(page)
        page = int(page)
    except PageNotAnInteger:
        page = 1
        list_items = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        list_items = paginator.page(page)
    if request.is_ajax():
        return TemplateResponse(request, 'blog/ajax_category.html', locals())
    return TemplateResponse(request, 'blog/category.html', locals())


def post(request, post_id, slug=None):
    post = get_object_or_404(Post, pk=post_id)
    related = Post.objects.filter(category=post.category).exclude(id=post_id)[:3]
    return TemplateResponse(request, 'blog/article.html', locals())
