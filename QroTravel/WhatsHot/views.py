from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import get_language, ugettext_lazy as _
from django.template.response import TemplateResponse
from django.urls import reverse
from django.conf import settings
from django.http import Http404
from django.db.models import Q

from .models import *
from .forms import *
from .utils import model_dict
from Blog.models import Post
from Events.models import Event
from Regions.models import Section as RegionsSection

PAGINATOR_ITEMS = getattr(settings, 'PAGINATOR_ITEMS', 9)


def landing(request, category_id, slug=None):
    instance = get_object_or_404(
        Category.objects.prefetch_related('sections'),
        pk=category_id
    )
    filter_form = CategoryOptionsFilterForm(instance, request.POST or None)
    if instance.has_sections:
        qs = instance.sections.all() | instance.main_sections.all()
    else:
        qs = instance.cards.all()
        href = reverse('WhatsHot:landing', args=[instance.id, instance.slug])
    if filter_form.is_valid():
        for field in filter_form.cleaned_data:
            if filter_form.cleaned_data[field]:
                qs = qs.filter(category_filters__in=filter_form.cleaned_data[field])
    qs = qs.distinct()
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
    if instance.has_sections:
        if request.is_ajax():
            return TemplateResponse(request, 'whatshot/ajax_what_to_do_landing.html', locals())
        return TemplateResponse(request, 'whatshot/what_to_do_landing.html', locals())
    else:
        if request.is_ajax():
            return TemplateResponse(request, 'whatshot/ajax_what_to_do.html', locals())
        return TemplateResponse(request, 'whatshot/what_to_do.html', locals())


def section(request, section_id, slug=None):
    instance = get_object_or_404(
        Section.objects.prefetch_related('cards'),
        pk=section_id
    )
    qs = instance.cards.all()
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
    href = reverse('WhatsHot:section', args=[instance.id, instance.slug])
    if request.is_ajax():
        return TemplateResponse(request, 'whatshot/ajax_what_to_do.html', locals())
    return TemplateResponse(request, 'whatshot/what_to_do.html', locals())


def card(request, card_id, slug=None):
    card = get_object_or_404(
        Card.objects.prefetch_related('card_photos'),
        pk=card_id
    )
    return TemplateResponse(request, 'whatshot/card.html', locals())


def search(request, model=None, category_id=None):
    query = request.GET.get('query', '')
    aux = None
    LANGUAGE = get_language()
    if query:
        if model is None:
            q_func = model_dict.MODEL_Q_FUNC('Card', query, LANGUAGE, split=False)
            qs_1 = Card.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Section', query, LANGUAGE, split=False)
            qs_2 = RegionsSection.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Post', query, LANGUAGE, split=False)
            qs_3 = Post.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Event', query, LANGUAGE, split=False)
            qs_4 = Event.objects.filter(q_func).distinct()
            aux = list(qs_1) + list(qs_2) + list(qs_3) + list(qs_4)
            q_func = model_dict.MODEL_Q_FUNC('Card', query, LANGUAGE)
            qs_1 = Card.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Section', query, LANGUAGE)
            qs_2 = RegionsSection.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Post', query, LANGUAGE)
            qs_3 = Post.objects.filter(q_func).distinct()
            q_func = model_dict.MODEL_Q_FUNC('Event', query, LANGUAGE)
            qs_4 = Event.objects.filter(q_func).distinct()
            aux += list(qs_1) + list(qs_2) + list(qs_3) + list(qs_4)
        elif category_id:
            category_id = int(category_id)
            model_str = model.__name__
            q_func = model_dict.MODEL_Q_FUNC(model_str, query, LANGUAGE, split=False)
            qs = model.objects.filter(q_func).filter(category__id=category_id).distinct()
            aux = list(qs)
            q_func = model_dict.MODEL_Q_FUNC(model_str, query, LANGUAGE)
            qs = model.objects.filter(q_func).filter(category__id=category_id).distinct()
            aux += list(qs)
        else:
            model_str = model.__name__
            q_func = model_dict.MODEL_Q_FUNC(model_str, query, LANGUAGE, split=False)
            qs = model.objects.filter(q_func).distinct()
            aux = list(qs)
            q_func = model_dict.MODEL_Q_FUNC(model_str, query, LANGUAGE)
            qs = model.objects.filter(q_func).distinct()
            aux += list(qs)
    if aux:
        paginator = Paginator(aux, PAGINATOR_ITEMS)
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
        r_pages = range(1, paginator.num_pages+1)
    return TemplateResponse(request, 'search/results.html', locals())
