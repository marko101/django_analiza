# Generated by Django 4.1.7 on 2023-04-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('Region', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Polutant',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('removed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'polutions',
            },
        ),
        migrations.CreateModel(
            name='PolutantEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('annual_PM10', models.IntegerField()),
                ('year', models.IntegerField()),
                ('type', models.CharField(blank=True, default='', max_length=100)),
                ('Temporal_coverage', models.CharField(blank=True, default='', max_length=100)),
                ('Reference', models.CharField(blank=True, default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='airpolution.country')),
                ('polutant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='airpolution.polutant')),
            ],
            options={
                'verbose_name_plural': 'polutant entry',
            },
        ),
    ]
