from modeltranslation.translator import translator, TranslationOptions
from Visitor.models import *

class ConfigurationTranslationOptions(TranslationOptions):
    fields = (
            'title', 'subtitle', 'location_description', 'sub_heading', 'section_name',
            'arrive_description', 'weather_description', 'sub_heading_title',
            'meta_description', 'meta_keywords',
        )

class QueretaroLandingTranslationOptions(TranslationOptions):
    fields = (
            'title', 'excerpt', 'heading', 'description', 'faqs_text',
            'meta_description', 'meta_keywords',
        )

class QueretaroSectionTranslationOptions(TranslationOptions):
    fields = (
            'title', 'sub_title', 'excerpt', 'button_text', 'button_link',
        )

class SeasonTranslationOptions(TranslationOptions):
    fields =('title', 'description',)

class SectionTranslationOptions(TranslationOptions):
    fields =(
            'title', 'sub_title', 'sub_heading', 'heading',
            'button_section_text',
            )

class TransportationTypeTranslationOptions(TranslationOptions):
    fields =('title', 'description',)

translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(QueretaroLanding, QueretaroLandingTranslationOptions)
translator.register(QueretaroSection, QueretaroSectionTranslationOptions)
translator.register(Season, SeasonTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(TransportationType, TransportationTypeTranslationOptions)