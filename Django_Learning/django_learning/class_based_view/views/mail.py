from django.views.generic import FormView
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy
from ..forms import ContactForm

def contactview(request):
    form_class = ContactForm
    # name = form.cleaned_data['name']
    # email = form.cleaned_data['email']
    # message = form.cleaned_data['message']
    subject = 'New contact form submission'
    message = 'Test mail by django server'
    from_mail = 'prabakarann.2702@gmail.com'
    to_mail = ['prabakarann.2702@gmail.com']
    
    send_mail( subject, message, from_mail, to_mail, fail_silently=False )

    # email_message = EmailMessage(subject, body, from_email, to_email)
    # email_message.send()
    return render(request, 'contact.html', {'form':form_class})


