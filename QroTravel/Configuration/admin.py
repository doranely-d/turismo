from django.contrib.admin.sites import AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *


@admin.register(Home)
class HomeAdmin(SingletonModelAdmin):
    # form = MultilingualModelForm
    fieldsets = (
        (_('General Data'),
            {
                'fields': (
                    'discover',
                )
            }
        ),
        (_('QroTravel URLs'),
            {
                'fields': (
                    'promotions', 'reserve', 'occ',
                )
            }
        ),
        (_('Social URLs'),
            {
                'fields': (
                    'instagram_url', 'facebook_url', 'twitter_url',
                )
            }
        ),
        (_('Contact email'),
            {
                'fields': (
                    'contact_email',
                )
            }
        ),
        (_('Search section configuration'),
            {
                'fields': (
                    'search_title', 'search_title_en', 'search_title_fr',
                    'search_subtitle', 'search_subtitle_en', 'search_subtitle_fr',
                    'search_banner_image'
                )
            }
        ),
        (_('Error page configuration'),
            {
                'fields': (
                    'error_banner_image',
                )
            }
        ),
        (_('Analytics'),
            {
                'fields': (
                    'google_analytics',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                )
            }
        ),
        (_('Privacy policy'), {'fields': ('privacy_policy_banner_image', 'privacy_policy', 'privacy_policy_en', 'privacy_policy_fr',)}),
        (_('Transparency'), {'fields': ('transparency_banner_image', 'transparency', 'transparency_en', 'transparency_fr')}),
    )


myapp = apps.get_app_config('Configuration')
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


from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
admin.site.unregister(Group)
admin.site.unregister(Site)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
