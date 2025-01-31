# Generated by Django 5.0.6 on 2024-10-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_page_theme_alter_theme_backimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='jscript',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
