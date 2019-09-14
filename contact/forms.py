from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class ContactForm(forms.Form):
        name = forms.CharField(label='Enter your name', max_length=100)
        mobile = forms.CharField(label='Contact Number', max_length=15)
        email = forms.EmailField(label='Enter your email', max_length=100)
        message = forms.CharField(widget=forms.Textarea(
            attrs={'width': "100%", 'cols': "40", 'rows': "5", }))

