# Generated by Django 2.2.4 on 2019-08-27 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20190826_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]
