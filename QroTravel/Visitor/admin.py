from django.contrib.admin.sites import AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *
from .admin_forms import *


@admin.register(Configuration)
class ConfigurationAdmin(SingletonModelAdmin):
    fieldsets = (
        (_('Landing Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'section_name', 'section_name_en', 'section_name_fr',
                    'subtitle', 'subtitle_en', 'subtitle_fr',
                    'banner_image',
                )
            }
        ),
        (_('Location Data'),
            {
                'fields': (
                    'location_description', 'location_description_en', 'location_description_fr',
                    'sub_heading', 'sub_heading_en', 'sub_heading_fr',
                    'sub_heading_title', 'sub_heading_title_en', 'sub_heading_title_fr',
                    'location_image',
                )
            }
        ),
        (_('How to arrive Data'),
            {
                'fields': (
                    'arrive_description', 'arrive_description_en', 'arrive_description_fr',
                    'background_arrive_image',
                )
            }
        ),
        (_('Weather Data'),
            {
                'fields': (
                    'weather_description', 'weather_description_en', 'weather_description_fr',
                )
            }
        ),
    )
    form = ConfigurationAdminForm


@admin.register(QueretaroSection)
class QueretaroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    form = QueretaroSectionAdminForm


@admin.register(QueretaroLanding)
class QueretaroLandingAdmin(SingletonModelAdmin):
    fieldsets = (
        (_('Landing Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'excerpt', 'excerpt_en', 'excerpt_fr',
                    'banner_image',
                )
            }
        ),
        (_('Landing Extra Data'),
            {
                'fields': (
                    'heading', 'heading_en', 'heading_fr',
                    'description', 'description_en', 'description_fr',
                    'image', 'faqs_text', 'faqs_text_en', 'faqs_text_fr',
                    'show_faqs_text',
                )
            }
        ),
    )
    form = QueretaroLandingAdminForm


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm


myapp = apps.get_app_config('Visitor')
for model in myapp.get_models(include_auto_created=False):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
# for model in myapp.get_models(include_auto_created=False):
#     try:
#         if issubclass(model, MultilingualModel):
#             model_admin = type("%sAdmin" % model, (admin.ModelAdmin,), {
#                 'form': MultilingualModelForm,
#             })
#             admin.site.register(model, model_admin)
#         else:
#             admin.site.register(model)
#     except AlreadyRegistered:
#         pass
