# Generated by Django 3.2 on 2022-12-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0012_auto_20221016_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piclist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
