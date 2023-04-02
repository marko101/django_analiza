# Generated by Django 4.1.7 on 2023-03-30 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slicice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=64, unique=True)),
                ('opis', models.TextField(blank=True, default='')),
                ('kreirano', models.DateTimeField(auto_now_add=True)),
                ('kreirao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slicice', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'moja aplikacija',
                'ordering': ['ime'],
            },
        ),
    ]
