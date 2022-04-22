# Generated by Django 4.0.3 on 2022-04-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_channel_fasta'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='featureset',
            field=models.TextField(blank=True, help_text='Array of features in text for visualizing annotations. null ok', max_length=5000, null=True),
        ),
    ]
