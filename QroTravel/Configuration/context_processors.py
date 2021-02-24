from .models import Home
from WhatsHot.models import Category
from Regions.models import Region
from Visitor.models import Configuration


def home_context(request):
    """
    Metodo que incluye las categorias principales disponibles en todos los templates
    """
    return {
        'CONFIGURATION': Home.objects.get(),
        'CATEGORIES': Category.objects.all(),
        'REGIONS': Region.objects.all(),
        'VISITORS_CONFIGURATION': Configuration.objects.get(),
    }
