import re

from django.conf import settings
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    def create_user(self,
                    name,
                    email,
                    mobile=None,
                    message=None):
        # if not email:
        #     raise ValueError('Enter a valid email address')
        # if not re.match(r'\d{10}$', mobile):
        #     raise ValueError('Enter a valid mobile number')

        user = self.model(
            name=name,
            email=email,
            mobile=mobile,
            message=message
        )
        user.save(using=self._db)
        return user



    name = models.CharField(max_length=30)
    email = models.CharField(blank=True, max_length=200)
    message = models.TextField(max_length=1000, default=None, blank=True,
                               null=True)
    mobile = models.CharField(null=False, blank=False, unique=True,
                              max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Contact, related_name="post_author",
                               on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
