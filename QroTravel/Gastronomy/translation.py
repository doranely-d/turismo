from modeltranslation.translator import translator, TranslationOptions
from Gastronomy.models import *

class GastronomyLandingTranslationOptions(TranslationOptions):
    fields = (
            'title', 'excerpt', 'heading', 'description',
            'meta_description', 'meta_keywords', 'image_alt_text',
        )

class GastronomySectionTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'excerpt', 'button_text',)


translator.register(GastronomyLanding, GastronomyLandingTranslationOptions)
translator.register(GastronomySection, GastronomySectionTranslationOptions)