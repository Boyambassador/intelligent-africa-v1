# Generated by Django 4.0.6 on 2022-07-22 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
