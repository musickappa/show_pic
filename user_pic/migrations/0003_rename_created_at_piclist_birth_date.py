# Generated by Django 3.2 on 2022-09-10 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0002_alter_piclist_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piclist',
            old_name='created_at',
            new_name='birth_date',
        ),
    ]