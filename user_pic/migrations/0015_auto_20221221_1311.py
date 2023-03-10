# Generated by Django 3.2 on 2022-12-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0014_alter_piclist_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('family_name', models.CharField(blank=True, max_length=50, null=True)),
                ('career', models.CharField(blank=True, max_length=50, null=True)),
                ('feature', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'プロフィール',
            },
        ),
        migrations.RenameField(
            model_name='piclist',
            old_name='last_name',
            new_name='family_name',
        ),
    ]
