from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm

from .models import *


class FooterSubLinkInline(admin.TabularInline):
    # form = MultilingualModelForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'link', 'link_en', 'link_fr',
                    'order', 'new_window', 'active',
                )
            }
        ),
    )
    model = FooterSubLink
    extra = 0


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    # form = MultilingualModelForm
    inlines = [FooterSubLinkInline]


myapp = apps.get_app_config('Menus')
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

admin.site.unregister(FooterSubLink)
