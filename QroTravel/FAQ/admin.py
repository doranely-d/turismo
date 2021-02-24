from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *


@admin.register(Configuration)
class HomeAdmin(SingletonModelAdmin):
    # form = MultilingualModelForm
    fielsets = (
        (_('General Data'), {
            'fields': (
                'title', 'title_en', 'title_fr',
                'description', 'description_en', 'description_fr',
                'meta_description', 'meta_description_en', 'meta_description_fr',
                'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                'banner_image'
            )
        })
    )


myapp = apps.get_app_config('FAQ')
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
