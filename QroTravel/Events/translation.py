from modeltranslation.translator import translator, TranslationOptions
from Events.models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = (
            'name',
            )

class ConfigurationTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'meta_description', 'meta_keywords',)

class EventTranslationOptions(TranslationOptions):
    fields = (
            'title', 'slug', 'subtitle', 'excerpt', 'content',
            'meta_description', 'meta_keywords', 'image_alt_text',
        )

class EventPhotoTranslationOptions(TranslationOptions):
    fields = ('alt_text',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(EventPhoto, EventPhotoTranslationOptions)