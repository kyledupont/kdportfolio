from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from forms import ContactForm
import sendgrid
import os
from sendgrid.helpers.mail import *
from keys import SENDGRID_API_KEY
from sendemail import send_email


# def home(request):
#     return render(request, "index.html")

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_email(name, email, message)
            code = send_email.code
            messages.add_message(request, messages.SUCCESS, 'Form submission successful!')
            form.save()
            form = ContactForm()
            args = {'form': form, 'name': name, 'email': email, 'message': message, 'code': code}
            return render(request, 'index.html', args)

            # send_email()
            # pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
        return render(request, 'index.html', {'form': form})
