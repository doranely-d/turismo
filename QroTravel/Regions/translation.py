from modeltranslation.translator import translator, TranslationOptions
from Regions.models import *

class ConfigurationTranslationOptions(TranslationOptions):
    fields = (
            'title', 'subtitle', 'sub_regions_heading',
            'sub_regions_sub_heading', 'meta_description', 'meta_keywords',
            'sub_regions_image_alt_text',
        )

class RegionTranslationOptions(TranslationOptions):
    fields = (
            'title', 'slug', 'sub_title', 'sub_heading', 'heading',
            'extra_data', 'button_text', 'meta_description', 'meta_keywords',
            'sub_banner_image_alt_text',
        )

class SectionTranslationOptions(TranslationOptions):
    fields = (
            'title', 'slug', 'sub_title', 'sub_heading', 'button_text',
            'content', 'excerpt', 'meta_description', 'meta_keywords',
        )

class SectionPhotoTranslationOptions(TranslationOptions):
    fields =('alt_text',)

translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(Region, RegionTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(SectionPhoto, SectionPhotoTranslationOptions)