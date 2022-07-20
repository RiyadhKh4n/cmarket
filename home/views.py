from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm1


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def displayPrivacyPolicy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def displayTermsConditions(request):
    """ A view to return the T&Cs page """

    return render(request, 'home/terms-and-conditions.html')


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm1(request.POST)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        sender = "Contact request from" + " " + str(email)
        msg_mail = str(message) + ", " + str(sender)
        if form.is_valid():
            send_mail(
                subject,
                msg_mail,
                email,
                [settings.DEFAULT_FROM_EMAIL, ]
            )
            form.save()
            messages.success(request, 'Your Email has been sent !!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'There Was an Error Trying to Send Email Message,\
                    Please check your form.'
            )
    else:
        form = ContactForm1()
    context = {'form': form}
    return render(request, 'home/contact.html', context)

