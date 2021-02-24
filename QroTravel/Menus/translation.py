from modeltranslation.translator import translator, TranslationOptions
from Menus.models import *

class FooterLinkTranslationOptions(TranslationOptions):
    fields = ('title', 'link',)

class FooterSubLinkTranslationOptions(TranslationOptions):
    fields = ('title', 'link',)

translator.register(FooterLink, FooterLinkTranslationOptions)
translator.register(FooterSubLink, FooterSubLinkTranslationOptions)