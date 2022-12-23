# Generated by Django 3.2 on 2022-12-21 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_pic', '0016_myprofile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='profile_img',
            field=models.ImageField(default='user_pic/img/kappa_icon.jpg', null=True, upload_to='user_pic/img'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='family_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]