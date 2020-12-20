# Generated by Django 3.1.4 on 2020-12-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeheads', '0002_auto_20201209_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='estimated_price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='opinion',
            name='acidity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='opinion',
            name='bitterness',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='opinion',
            name='body',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='opinion',
            name='flavor',
            field=models.IntegerField(default=0),
        ),
    ]
