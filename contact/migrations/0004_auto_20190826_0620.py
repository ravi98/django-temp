# Generated by Django 2.2.4 on 2019-08-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
