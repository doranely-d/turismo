from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *
from .admin_forms import *


class EventPhotoInline(admin.TabularInline):
    # form = MultilingualModelForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'image', 'alt_text', 'alt_text_en', 'alt_text_fr', 'order',
                )
            }
        ),
    )
    model = EventPhoto
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventPhotoInline]
    prepopulated_fields = {'slug': ('title',), 'slug_en': (
        'title_en',), 'slug_fr': ('title_fr',)}
    form = EventAdminForm


@admin.register(Configuration)
class HomeAdmin(SingletonModelAdmin):
    # form = MultilingualModelForm
    fielsets = (
        (_('General Data'), {
            'fields': (
                'title', 'title_en', 'title_fr',
                'excerpt', 'excerpt_en', 'excerpt_fr',
                'meta_description', 'meta_description_en', 'meta_description_fr',
                'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                'banner_image'
            )
        })
    )


myapp = apps.get_app_config('Events')
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


admin.site.unregister(EventPhoto)
