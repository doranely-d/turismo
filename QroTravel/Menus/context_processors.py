from .models import *


def links_context(request):
    """
    Metodo que incluye los links de header y footer disponibles en todos los templates
    """
    return {
        'FOOTER_MENUS': FooterLink.objects.prefetch_related('sublinks').filter(active=True),
    }


def external_links_context(request):
    return {
        'EXTERNAL_LINKS': ExternalLink.objects.display()
    }
