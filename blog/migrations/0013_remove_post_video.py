# Generated by Django 4.0.6 on 2022-08-01 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_video_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
