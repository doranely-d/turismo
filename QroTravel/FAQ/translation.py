from modeltranslation.translator import translator, TranslationOptions
from FAQ.models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug',)

class ConfigurationTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'meta_description', 'meta_keywords',)

class QuestionTranslationOptions(TranslationOptions):
    fields = ('title', 'answer',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Configuration, ConfigurationTranslationOptions)
translator.register(Question, QuestionTranslationOptions)