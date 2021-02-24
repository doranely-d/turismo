from django.contrib.admin.sites import AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *


@admin.register(Configuration)
class ConfigurationAdmin(SingletonModelAdmin):
    # form = MultilingualModelForm
    fieldsets = (
        (_('General Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'subtitle', 'subtitle_en', 'subtitle_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'excerpt', 'excerpt_en', 'excerpt_fr',
                    'description', 'description_en', 'description_fr',
                )
            }
        ),
        (_('Extra'),
            {
                'fields': (
                    'banner_image', 'web_site',
                )
            }
        ),
        (_('Magazine'),
            {
                'fields': (
                    'magazine_image', 'magazine_url', 'magazine_image_alt_text',
                    'magazine_image_alt_text_en', 'magazine_image_alt_text_fr',
                )
        }
        ),
    )

myapp = apps.get_app_config('Asomarte')
for model in myapp.get_models(include_auto_created=False):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

# myapp = apps.get_app_config('Asomarte')
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
