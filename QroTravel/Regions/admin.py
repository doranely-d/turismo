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
    # form = MultilingualModelForm
    fieldsets = (
        (_('Landing Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'subtitle', 'subtitle_en', 'subtitle_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'banner_image',
                )
        }
        ),
        (_('Regions General Data'),
            {
                'fields': (
                    'sub_regions_sub_heading', 'sub_regions_sub_heading_en', 'sub_regions_sub_heading_fr',
                    'sub_regions_heading', 'sub_regions_heading_en', 'sub_regions_heading_fr',
                    'sub_regions_image', 'sub_regions_image_alt_text', 'sub_regions_image_alt_text_en',
                    'sub_regions_image_alt_text_fr',
                )
        }
        ),
    )


class SectionPhotoInline(admin.TabularInline):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'image', 'order', 'alt_text', 'alt_text_en', 'alt_text_fr',
                )
            }
        ),
    )
    model = SectionPhoto
    extra = 0


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_prefetch_related = ('region', )
    inlines = [SectionPhotoInline]
    list_filter = ['region']
    search_fields = ('title',)
    form = SectionAdminForm
    prepopulated_fields = {
        'slug': ('title',),
        'slug_en': ('title_en',),
        'slug_fr': ('title_fr',)
    }
    fieldsets = (
        (_('General Data'),
            {
                'fields': (
                    'region',
                    'title', 'title_en', 'title_fr',
                    'slug', 'slug_en', 'slug_fr',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'content', 'content_en', 'content_fr',
                    'sub_title', 'sub_title_en', 'sub_title_fr',
                    'sub_heading', 'sub_heading_en', 'sub_heading_fr',
                    'excerpt', 'excerpt_en', 'excerpt_fr',
                    'button_text', 'button_text_en', 'button_text_fr',
                    'link', 'blank',
                    'address', 'web_site', 'contact_email',
                    'instagram_url', 'twitter_url', 'facebook_url',
                    'phone_1', 'phone_2', 'phone_3',
                    'google_maps', 'banner_image',
                    'order',
                )
        }
        ),
    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)
    }
    fieldsets = (
        (_('General Data'),
            {
                'fields': (
                    'title', 'title_en', 'title_fr',
                    'title_color',
                    'meta_description', 'meta_description_en', 'meta_description_fr',
                    'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
                    'slug', 'slug_en', 'slug_fr',
                    'sub_title', 'sub_title_en', 'sub_title_fr',
                    'heading', 'heading_en', 'heading_fr',
                    'sub_heading', 'sub_heading_en', 'sub_heading_fr',
                    'extra_data', 'extra_data_en', 'extra_data_fr',
                    'banner_image', 'sub_banner_image', 'sub_banner_image_alt_text',
                    'sub_banner_image_alt_text_en', 'sub_banner_image_alt_text_fr',
                    'button_text',
                )
        }
        ),
    )
    form = RegionAdminForm


myapp = apps.get_app_config('Regions')
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

admin.site.unregister(SectionPhoto)
