# Generated by Django 3.2 on 2022-09-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0004_auto_20220910_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piclist',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
