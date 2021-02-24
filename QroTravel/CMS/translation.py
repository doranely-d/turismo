from modeltranslation.translator import translator, TranslationOptions
from CMS.models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ContactGroupTranslationOptions(TranslationOptions):
    fields = (
            'name',
        	)

class ContactTranslationOptions(TranslationOptions):
    fields = (
            'title', 'excerpt', 'description', 'meta_description', 'meta_keywords',
            )

class InspirationTranslationOptions(TranslationOptions):
    fields = ('title', 'image_alt_text',)

class SlideTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)
translator.register(ContactGroup, ContactGroupTranslationOptions)
translator.register(Contact, ContactTranslationOptions)
translator.register(Inspiration, InspirationTranslationOptions)
translator.register(Slide, SlideTranslationOptions)