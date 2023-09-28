# Generated by Django 4.1 on 2023-09-16 08:09

import core.title
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='success',
            field=models.CharField(default=core.title.generate_short_id, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]