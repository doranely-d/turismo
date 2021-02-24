from modeltranslation.translator import translator, TranslationOptions
from Blog.models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = (
            'name', 'slug', 'description', 'meta_description', 'meta_keywords',
            'thumbnail_image_alt_text',
        	)

class ConfigurationTranslationOptions(TranslationOptions):
    fields = (
            'categories_title', 'category_title', 'meta_description', 'meta_keywords',
        	)

class PostTranslationOptions(TranslationOptions):
    fields = (
            'title', 'slug', 'subtitle', 'excerpt', 'content',
            'meta_description', 'meta_keywords', 'post_image_alt_text',
        )


translator.register(Category, CategoryTranslationOptions)
translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(Post, PostTranslationOptions)