from modeltranslation.translator import translator, TranslationOptions
from WhatsHot.models import *

class CardTranslationOptions(TranslationOptions):
    fields = (
            'title', 'subtitle', 'description', 'button_text', 'subheading',
            'slug', 'excerpt', 'button_360_text', 'meta_description', 'meta_keywords',
        )


class CategoryFilterTranslationOptions(TranslationOptions):
    fields = ('name',)

class CategoryFilterOptionTranslationOptions(TranslationOptions):
    fields =('name',)

class SectionTranslationOptions(TranslationOptions):
    fields =(
            'title', 'description', 'slug', 'meta_description', 'meta_keywords',
        )

class CategoryTranslationOptions(TranslationOptions):
    fields =(
            'title', 'name', 'description', 'slug', 'meta_description', 'meta_keywords',
        )

class KeywordTranslationOptions(TranslationOptions):
    fields =('name',)

translator.register(Card, CardTranslationOptions)
translator.register(CategoryFilter, CategoryFilterTranslationOptions)
translator.register(CategoryFilterOption, CategoryFilterOptionTranslationOptions)
translator.register(Section, SectionTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Keyword, KeywordTranslationOptions)