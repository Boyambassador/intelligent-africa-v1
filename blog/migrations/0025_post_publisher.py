# Generated by Django 4.0.5 on 2022-11-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_post_video_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]