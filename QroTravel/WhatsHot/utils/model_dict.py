from django.db.models import Q
import re


# Card q_func
def q_func_c(q, language):
    q_funcs = {
        'es': (
            Q(title__icontains=q) | Q(description__icontains=q) |
            Q(subheading__icontains=q) | Q(subtitle__icontains=q) |
            Q(sections__title__icontains=q) | Q(keywords__name__icontains=q)
        ),
        'en': (
            Q(title_en__icontains=q) | Q(description_en__icontains=q) |
            Q(subheading_en__icontains=q) | Q(subtitle_en__icontains=q) |
            Q(sections__title_en__icontains=q) | Q(keywords__name_en__icontains=q)
        ),
        'fr': (
            Q(title_fr__icontains=q) | Q(description_fr__icontains=q) |
            Q(subheading_fr__icontains=q) | Q(subtitle_fr__icontains=q) |
            Q(sections__title_fr__icontains=q) | Q(keywords__name_fr__icontains=q)
        ),
    }
    return q_funcs[language]


# Event and Post q_func
def q_func_ep(q, language):
    q_funcs = {
        'es': (
            Q(title__icontains=q) | Q(excerpt__icontains=q) |
            Q(content__icontains=q) | Q(subtitle__icontains=q)
        ),
        'en': (
            Q(title_en__icontains=q) | Q(excerpt_en__icontains=q) |
            Q(content_en__icontains=q) | Q(subtitle_en__icontains=q)
        ),
        'fr': (
            Q(title_fr__icontains=q) | Q(excerpt_fr__icontains=q) |
            Q(content_fr__icontains=q) | Q(subtitle_fr__icontains=q)
        ),
    }
    return q_funcs[language]


# Section q_func
def q_func_s(q, language):
    q_funcs = {
        'es': (
            Q(title__icontains=q) | Q(content__icontains=q) |
            Q(sub_heading__icontains=q) | Q(sub_title__icontains=q) |
            Q(region__title__icontains=q) | Q(region__sub_title__icontains=q) |
            Q(region__heading__icontains=q) | Q(region__sub_heading__icontains=q)
        ),
        'en': (
            Q(title_en__icontains=q) | Q(content_en__icontains=q) |
            Q(sub_heading_en__icontains=q) | Q(sub_title_en__icontains=q) |
            Q(region__title_en__icontains=q) | Q(region__sub_title_en__icontains=q) |
            Q(region__heading_en__icontains=q) | Q(region__sub_heading_en__icontains=q)
        ),
        'fr': (
            Q(title_fr__icontains=q) | Q(content_fr__icontains=q) |
            Q(sub_heading_fr__icontains=q) | Q(sub_title_fr__icontains=q) |
            Q(region__title_fr__icontains=q) | Q(region__sub_title_fr__icontains=q) |
            Q(region__heading_fr__icontains=q) | Q(region__sub_heading_fr__icontains=q)
        ),
    }
    return q_funcs[language]


def MODEL_Q_FUNC(class_s, query, language, split=True):
    if language is None:
        language = 'es'
    # Function
    model_dict = {
        'Section': q_func_s,
        'Post': q_func_ep,
        'Event': q_func_ep,
        'Card': q_func_c,
    }
    q_func = model_dict[class_s]
    aux_q = None
    if split:
        query = re.sub("[^\w]", " ",  query).split()
        for q in query:
            aux_q = aux_q & q_func(q, language) if aux_q else q_func(q, language)
    else:
        aux_q = q_func(query, language)
    return aux_q
