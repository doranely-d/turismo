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
        (_('General Data'), {'fields': (
            'outstanding_post',
            'meta_description', 'meta_description_en', 'meta_description_fr',
            'meta_keywords', 'meta_keywords_en', 'meta_keywords_fr',
            'category_title', 'category_title_en', 'category_title_fr',
            'categories_title', 'categories_title_en', 'categories_title_fr',
        )}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)}
    form = PostAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), 'slug_en': ('name_en',), 'slug_fr': ('name_fr',)}
    # form = MultilingualModelForm


myapp = apps.get_app_config('Blog')
for model in myapp.get_models(include_auto_created=False):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass


# myapp = apps.get_app_config('Blog')
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
