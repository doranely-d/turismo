from django.template.response import TemplateResponse


def privacy_policy(request):
    return TemplateResponse(request, 'configuration/privacy_policy.html', locals())


def transparency(request):
    return TemplateResponse(request, 'configuration/transparency.html', locals())
