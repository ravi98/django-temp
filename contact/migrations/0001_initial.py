# Generated by Django 2.2.4 on 2019-08-26 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('email', models.CharField(blank=True, max_length=200)),
                ('mobile', models.IntegerField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]