# Generated by Django 4.0.5 on 2022-09-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_document_alter_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='details',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]