from django.shortcuts import render, reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .contact_email import AutoMail

def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print('form is valid')
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                AutoMail.contact_us('','','')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('email_success')
    return render(request, "contact_us.html", {'form': form})

def successView(request):
    #return HttpResponse('Success! Thank you for your message.')
    messages.success(request, "Thanks for your message!")
    return redirect(reverse('index'))