# Generated by Django 3.2 on 2022-12-21 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0017_auto_20221221_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='family_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='profile_img',
            field=models.ImageField(default='user_pic/img/kappa_icon.jpg', null=True, upload_to='user_pic/img', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpeg', 'jpg', 'mp4'])]),
        ),
        migrations.AlterField(
            model_name='piclist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_pic/img', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpeg', 'jpg', 'mp4'])]),
        ),
    ]