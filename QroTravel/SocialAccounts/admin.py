from django.contrib.admin.sites import AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.apps import apps

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm
from solo.admin import SingletonModelAdmin

from .models import *
from .admin_forms import *


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    form = FeedAdminForm


myapp = apps.get_app_config('SocialAccounts')
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


admin.site.unregister(Feed)
