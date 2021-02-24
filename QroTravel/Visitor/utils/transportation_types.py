from django.utils.translation import ugettext_lazy as _


AIRPLANE = 'qro-travel-icon-plane'
BUS = 'qro-travel-icon-bus'
AUTOMOBILE = 'qro-travel-icon-auto'
TAXI = 'qro-travel-icon-taxi'

TRANSPORTATION_TYPE_CHOICES = (
    (AIRPLANE, _('Airplane')),
    (BUS, _('Bus')),
    (AUTOMOBILE, _('Automobile')),
    (TAXI, _('Taxi')),
)
