# Generated by Django 5.0.6 on 2024-10-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_page_locked_page_private_page_unlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='passwd',
            field=models.CharField(default='', max_length=200),
        ),
    ]
