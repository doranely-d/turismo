from django.utils.translation import ugettext_lazy as _

from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

from django.forms.models import modelform_defines_fields, modelform_factory
from django.contrib.admin.utils import flatten_fieldsets
from django.core.exceptions import FieldError
from collections import OrderedDict
from functools import partial

# from linguo.models import MultilingualModel
# from linguo.forms import MultilingualModelForm

from .models import *
from .admin_forms import *


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order',]
    list_filter = ['categories',]
    form = SectionAdminForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(SectionAdmin, self).get_fieldsets(request, obj)
        main_category_id = None
        if obj:
            main_category_id = obj.main_category_id
            self.prepopulated_fields = {
                'slug_es': ('title_es',), 'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)
            }
        else:
            self.prepopulated_fields = {}
        if request.method == 'POST':
            main_category_id = request.POST.get('main_category', None)
            self.prepopulated_fields = {
                'slug_es': ('title_es',), 'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)
            }
        if main_category_id:
            try:
                main_category = Category.objects.get(pk=main_category_id)
            except:
                main_category_id = None
        if main_category_id is None:
            fieldsets = [
                (None, {'fields':
                    ['main_category']
                })
            ]
        else:
            original_fields = fieldsets[0][1]['fields']
            original_fields.remove('category_filters')
            original_fields.remove('main_category')
            original_fields.remove('categories')
            fields = ['main_category']
            if main_category.has_sections:
                fields.append('categories')
                fields += ['category_filter_option_%d' % d.id for d in main_category.filters.all()]
            fieldsets = [
                (_("Category Filters"), {'fields': fields}),
                ('Datos Generales', {'fields': original_fields}),
            ]
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        """
        Returns a Form class for use in the admin add view. This is used by
        add_view and change_view.
        """
        if 'fields' in kwargs:
            fields = kwargs.pop('fields')
        else:
            fields = flatten_fieldsets(self.get_fieldsets(request, obj))
        if self.exclude is None:
            exclude = []
        else:
            exclude = list(self.exclude)
        readonly_fields = self.get_readonly_fields(request, obj)
        exclude.extend(readonly_fields)
        if self.exclude is None and hasattr(self.form, '_meta') and self.form._meta.exclude:
            # Take the custom ModelForm's Meta.exclude into account only if the
            # ModelAdmin doesn't define its own.
            exclude.extend(self.form._meta.exclude)
        # if exclude is an empty list we pass None to be consistent with the
        # default on modelform_factory
        exclude = exclude or None

        # Remove declared form fields which are in readonly_fields.
        new_attrs = OrderedDict(
            (f, None) for f in readonly_fields
            if f in self.form.declared_fields
        )
        form = type(self.form.__name__, (self.form,), new_attrs)

        defaults = {
            "form": form,
            "fields": fields,
            "exclude": exclude,
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
        }
        defaults.update(kwargs)

        if defaults['fields'] is None and not modelform_defines_fields(defaults['form']):
            defaults['fields'] = forms.ALL_FIELDS

        if isinstance(defaults['fields'], list):
            fields = []
            for field in defaults['fields']:
                if not field.startswith('category_filter_option_'):
                    fields.append(field)
            defaults['fields'] = fields
        try:
            return modelform_factory(self.model, **defaults)
        except FieldError as e:
            raise FieldError('%s. Check fields/fieldsets/exclude attributes of class %s.'
                             % (e, self.__class__.__name__))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # form = MultilingualModelForm
    prepopulated_fields = {
        'slug': ('name',),
        'slug_es': ('name_es',),
        'slug_en': ('name_en',),
        'slug_fr': ('name_fr',)
    }

class CardPhotoInline(admin.TabularInline):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'image', 'order',
                )
            }
        ),
    )
    model = CardPhoto
    extra = 0


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title_es']
    list_filter = ['sections']
    search_fields = ('title_es',)
    form = CardAdminForm
    filter_horizontal = ['sections', 'keywords']

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CardAdmin, self).get_fieldsets(request, obj)
        category_id = None
        if obj:
            category_id = obj.category_id
            self.prepopulated_fields = {
                'slug_es': ('title_es',), 'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)
            }
            self.inlines = [CardPhotoInline]
        else:
            self.inlines = []
            self.prepopulated_fields = {}
        if request.method == 'POST':
            category_id = request.POST.get('category', None)
            self.prepopulated_fields = {
                'slug_es': ('title_es',), 'slug': ('title',), 'slug_en': ('title_en',), 'slug_fr': ('title_fr',)
            }
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
            except:
                category_id = None
        if category_id is None:
            fieldsets = [
                (None, {'fields':
                    ['category']
                })
            ]
        else:
            original_fields = fieldsets[0][1]['fields']
            original_fields.remove('category_filters')
            original_fields.remove('category')
            fields = ['category']
            if not category.has_sections:
                fields += ['category_filter_option_%d' % d.id for d in category.filters.all()]
            fieldsets = [
                (_("Category Filters"), {'fields': fields}),
                ('Datos Generales', {'fields': original_fields}),
            ]
        return fieldsets

    # def get_form(self, request, obj=None, **kwargs):
    #     """
    #     Returns a Form class for use in the admin add view. This is used by
    #     add_view and change_view.
    #     """
    #     if 'fields' in kwargs:
    #         fields = kwargs.pop('fields')
    #     else:
    #         fields = flatten_fieldsets(self.get_fieldsets(request, obj))
    #     if self.exclude is None:
    #         exclude = []
    #     else:
    #         exclude = list(self.exclude)
    #     readonly_fields = self.get_readonly_fields(request, obj)
    #     exclude.extend(readonly_fields)
    #     if self.exclude is None and hasattr(self.form, '_meta') and self.form._meta.exclude:
    #         # Take the custom ModelForm's Meta.exclude into account only if the
    #         # ModelAdmin doesn't define its own.
    #         exclude.extend(self.form._meta.exclude)
    #     # if exclude is an empty list we pass None to be consistent with the
    #     # default on modelform_factory
    #     exclude = exclude or None

    #     # Remove declared form fields which are in readonly_fields.
    #     new_attrs = OrderedDict(
    #         (f, None) for f in readonly_fields
    #         if f in self.form.declared_fields
    #     )
    #     form = type(self.form.__name__, (self.form,), new_attrs)

    #     defaults = {
    #         "form": form,
    #         "fields": fields,
    #         "exclude": exclude,
    #         "formfield_callback": partial(self.formfield_for_dbfield, request=request),
    #     }
    #     defaults.update(kwargs)

    #     if defaults['fields'] is None and not modelform_defines_fields(defaults['form']):
    #         defaults['fields'] = forms.ALL_FIELDS

    #     if isinstance(defaults['fields'], list):
    #         fields = []
    #         for field in defaults['fields']:
    #             if not field.startswith('category_filter_option_'):
    #                 fields.append(field)
    #         defaults['fields'] = fields
    #     try:
    #         return modelform_factory(self.model, **defaults)
    #     except FieldError as e:
    #         raise FieldError('%s. Check fields/fieldsets/exclude attributes of class %s.'
    #                          % (e, self.__class__.__name__))


class CategoryFilterOptionInline(admin.TabularInline):
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name_es', 'name_en', 'name_fr', 'order',
                )
            }
        ),
    )
    # form = MultilingualModelForm
    model = CategoryFilterOption
    extra = 0


@admin.register(CategoryFilter)
class CategoryFilterAdmin(admin.ModelAdmin):
    inlines = [CategoryFilterOptionInline]
    # form = MultilingualModelForm


myapp = apps.get_app_config('WhatsHot')
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

admin.site.unregister(CardPhoto)
admin.site.unregister(CategoryFilterOption)
