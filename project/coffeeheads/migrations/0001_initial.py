# Generated by Django 3.1.4 on 2021-01-10 12:27

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
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter full name of coffee', max_length=250)),
                ('origin', models.CharField(help_text='Enter coffee origin', max_length=100)),
                ('manufacturer', models.CharField(help_text='Enter coffee manufacturer', max_length=150)),
                ('description', models.TextField(blank=True, help_text='Enter coffee description')),
                ('average', models.FloatField(blank=True, default=0.0)),
                ('reviewed_by', models.IntegerField(blank=True, default=0)),
                ('image', models.ImageField(blank=True, default='img/default_coffee.jpg', null=True, upload_to='img')),
                ('estimated_price', models.FloatField(blank=True, default=0)),
                ('add_date', models.DateField(default='2021-01-10')),
            ],
            options={
                'verbose_name': 'coffee',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0, help_text='Enter coffee rating in scale 0-10')),
                ('opinion', models.TextField(blank=True, help_text='Describe your impressions with this coffee')),
                ('acidity', models.IntegerField(default=0)),
                ('body', models.IntegerField(default=0)),
                ('flavor', models.IntegerField(default=0)),
                ('bitterness', models.IntegerField(default=0)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeheads.coffee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(default='2021-01-10')),
                ('coffee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='coffeeheads.coffee')),
                ('opinion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coffeeheads.opinion')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
    ]
