# Generated by Django 4.2.7 on 2023-12-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_category_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='disabled',
        ),
        migrations.AddField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
