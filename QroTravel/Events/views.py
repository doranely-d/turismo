from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

from .models import *
from .forms import *

from datetime import datetime, date, timedelta

PAGINATOR_ITEMS = getattr(settings, 'PAGINATOR_ITEMS', 9)


def landing(request, year=None, month=None):
    all_events = request.GET.get('all_events', False)
    configuration = Configuration.objects.get()
    if year is None or month is None:
        today = date.today()
        all_events = 'all_events=%s' % all_events
        href = reverse('Events:month_landing', args=[today.year, str(today.month).zfill(2)])
        href = '%s?%s' % (href, all_events)
        return redirect(href)
    else:
        year = int(year)
        month = int(month)
    # Used only on template to display current, previous and next month for navigation
    relevant_date = date(year, month, 1)
    relevant_date_before = relevant_date - timedelta(days=10)
    relevant_date_after = relevant_date + timedelta(days=40)
    if all_events:
        aux_today = date.today()
        # Current month events
        q_func = (
            Q(start_date__gte=aux_today) | Q(end_date__gte=aux_today)
        )
    else:
        # Current month events
        q_func = (
            (Q(start_date__year=year) & (Q(start_date__month=month) | Q(end_date__month=month))) |
            (Q(start_date__lte=relevant_date) & Q(end_date__gte=relevant_date+timedelta(days=28)))
        )
    qs = Event.objects.filter(
        q_func,
        published=True,
    ).order_by('start_date')
    cat_ids = qs.values_list('category__id', flat=True)
    categories = Category.objects.filter(id__in=cat_ids)
    filter_form = CalendarFilterForm(qs, request.POST or None)
    if filter_form.is_valid():
        for field in filter_form.fields:
            if filter_form.cleaned_data[field]:
                qs = qs.filter(Q(**{filter_form.fields[field].filter_field+'__in': filter_form.cleaned_data[field]}))
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
    if request.is_ajax():
        return TemplateResponse(request, 'events/ajax_calendar.html', locals())
    return TemplateResponse(request, 'events/landing.html', locals())


def event(request, event_id, slug=None):
    evt = get_object_or_404(
        Event.objects.prefetch_related('event_photos'),
        pk=event_id
    )
    return TemplateResponse(request, 'events/event.html', locals())
