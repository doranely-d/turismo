from django.contrib.admin.sites import AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *
from .admin_forms import *


@admin.register(GastronomySection)
class GastronomySectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    form = GastronomySectionAdminForm


@admin.register(GastronomyLanding)
class GastronomyLandingAdmin(SingletonModelAdmin):
    # form = MultilingualModelForm
    fieldsets = (
        (_('Landing Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'excerpt', 'excerpt_en', 'excerpt_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'banner_image',
                )
        }
        ),
        (_('Landing Extra Data'),
            {
                'fields': (
                    'heading', 'heading_en', 'heading_fr',
                    'description', 'description_en', 'description_fr',
                    'image', 'image_alt_text', 'image_alt_text_en', 'image_alt_text_fr',
                )
        }
        ),
    )


myapp = apps.get_app_config('Gastronomy')
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
