from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
import os


import logging

logger = logging.getLogger(__name__)

def Send_mail(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        file = request.FILES.get('file')

        # send_mail.attach(email_instance.file.path)
        # file.attach(file.name,file.read,file.content)
        # file.send()
        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address] , file )
                
                fail_silently=False
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "page.html", context )


