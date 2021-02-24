from modeltranslation.translator import translator, TranslationOptions
from Asomarte.models import Configuration, Video

class ConfigurationTranslationOptions(TranslationOptions):
    fields = (
            'title', 'subtitle', 'excerpt', 'description',
            'meta_description', 'meta_keywords', 'magazine_image_alt_text',
        	)

class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt', 'image_alt_text',)

translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(Video, VideoTranslationOptions)