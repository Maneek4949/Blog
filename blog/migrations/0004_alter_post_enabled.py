# Generated by Django 4.2.7 on 2023-12-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_disabled_post_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
