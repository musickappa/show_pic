# Generated by Django 3.2 on 2022-10-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0009_auto_20220910_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piclist',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='piclist',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
