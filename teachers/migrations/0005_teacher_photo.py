# Generated by Django 2.2.7 on 2019-11-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20191125_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teachers'),
        ),
    ]
