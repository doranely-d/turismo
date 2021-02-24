from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings


def send_mail(template_name, recipients, context={}, attachments=None, reply_to=None, bcc=None):
    try:
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
        default_context = {
            'site_name': getattr(settings, 'SITE_NAME', ''),
            'domain': getattr(settings, 'DOMAIN_NAME', ''),
            'protocol': 'https' if getattr(settings, 'USE_HTTPS', False) else 'http',
        }
        context.update(default_context)
        subject = loader.render_to_string('emails/' + template_name + '.txt', context)
        subject = ''.join(subject.splitlines())
        email_content = loader.render_to_string('emails/' + template_name + '.html', context)
        if getattr(settings, 'EMAIL_HOST', '') == 'smtp.mandrillapp.com' and bcc:
            recipients = list(set(recipients + bcc))
            bcc = None
        email_message = EmailMessage(subject, email_content, from_email, recipients, reply_to=reply_to, bcc=bcc)
        email_message.content_subtype = "html"  # Main content is now text/html
        if attachments:
            for att in attachments:
                email_message.attach('%s.pdf' % att['name'], att['doc'], 'application/pdf')
        email_message.send(fail_silently=True)
    except TypeError:
        try:
            send_mail(template_name, recipients, context=context, attachments=attachments, reply_to=reply_to, bcc=bcc)
        except:
            pass
    except:
        pass
