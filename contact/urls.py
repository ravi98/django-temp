from django.conf.urls.static import static
from django.urls import path

from Tp import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('chef/', views.chef, name='chef'),
    path('submitContact', views.get_contact, name='formSubmit')
]
