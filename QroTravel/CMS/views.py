from django.template.response import TemplateResponse

from SocialAccounts.utils import feeds_types
from SocialAccounts.models import Feed
from WhatsHot.models import Section
from Events.models import Event
from .models import *
from .forms import *

from datetime import date


# Index
def google(request):
    return TemplateResponse(request, 'google.html')


def index(request):
    today = date.today()
    header_banners = Slide.objects.filter(display=True)
    inspirations = Inspiration.objects.all()[:6]
    outstanding_sections = Section.objects.filter(outstanding=True)
    events = Event.objects.filter(end_date__gte=today).order_by('start_date')[:3]
    # Regions models missing
    regions = None
    qs_social = Feed.objects.all()
    facebook_feed = qs_social.filter(feeds_type=feeds_types.FACEBOOK)[:1]
    tweets = qs_social.filter(feeds_type=feeds_types.TWITTER)[:2]
    instagrams = qs_social.filter(feeds_type=feeds_types.INSTAGRAM)[:4]
    return TemplateResponse(request, 'index.html', locals())


def contact(request):
    contact = Contact.objects.get()
    qs = Category.objects.prefetch_related('contacts').all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        valid = True
        form.save()
        form = ContactForm()
    return TemplateResponse(request, 'FAQ/contact.html', locals())
