# Generated by Django 4.0.6 on 2022-08-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
