# Generated by Django 4.0.5 on 2022-09-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumbnails',
            field=models.ImageField(null=True, upload_to='thumbnails'),
        ),
    ]