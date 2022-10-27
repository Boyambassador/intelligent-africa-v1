# Generated by Django 4.0.5 on 2022-10-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_post_image_post_body_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'zjc level Documents'), ('2', 'Olevel Documents'), ('3', 'Alevel Documents'), ('4', 'zjc Videos'), ('5', 'Olevel Videos'), ('6', 'Alevel Videos'), ('7', 'All documents'), ('8', 'All Videos')], default='1', max_length=8),
        ),
    ]
