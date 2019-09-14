import re
import traceback

from django.shortcuts import render
from django.utils import timezone
from rest_framework.renderers import JSONRenderer

from contact.serializers import ContactSerializer
from .models import Post, Contact
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def get_contact(request):
    try:
        if request.method == 'POST':
            myForm = ContactForm(request.POST)
            if myForm.is_valid():
                name = myForm.cleaned_data['name']
                email = myForm.cleaned_data['email']
                message = myForm.cleaned_data['message']
                email_from = settings.EMAIL_HOST_USER
                mobile = myForm.cleaned_data['mobile']
                message = str(mobile) +'   ' + message
                recipient_list = ['ravi.m@lendenclub.com']
                contact_serializer = ContactSerializer(
                    data={'mobile': mobile, 'email': email})
                # if not email:
                #     raise ValueError('Enter a valid email address')
                if contact_serializer.is_valid():
                    new_user = Contact.objects.create(name=name,
                                                      email=email,
                                                      mobile=mobile,
                                                      message=message
                                                      )
                    send_mail(name, message, email_from, recipient_list)
                messages.success(request, 'You are Noted Down, Hang ON!')
                # template = loader.get_template('contact/home.html')
            else:
                form = ContactForm()
            return render(request, 'contact/contact.html', {'form': myForm});
    except Exception as e:
        print(e, traceback.format_exc())
        return JSONResponse({'code': 500, 'response': 'Failed to signup'})


def home_page(request):
    return render(request, 'contact/home.html', {})


def about(request):
    return render(request, 'contact/about.html', {})


def contact(request):
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

    # return render(request, 'contact/contact.html', {})


def menu(request):
    return render(request, 'contact/menu.html', {})


def chef(request):
    return render(request, 'contact/chef.html', {})


@csrf_protect
def form_submit(request):
    # print(request.data)
    if request.method == "POST":
        post = form.save(commit=False)
        data = request.POST
        name = data.get('name')
        message = data.get('message')
        email = data.get('email')
        mobile = data.get('mobile')
        post=Contact.objects.create(
            name=name,
            email=email,
            message=message,
            mobile=mobile
        )
        post.save()

    return render(request, 'contact/contact.html', {})
