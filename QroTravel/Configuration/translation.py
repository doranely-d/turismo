from modeltranslation.translator import translator, TranslationOptions
from Configuration.models import *

class HomeTranslationOptions(TranslationOptions):
    fields = (
            'search_title', 'search_subtitle', 'privacy_policy', 'transparency',
            'meta_description', 'meta_keywords',
            )

translator.register(Home, HomeTranslationOptions)