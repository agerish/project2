# Generated by Django 4.2.3 on 2023-07-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0019_evenement'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='image',
            field=models.ImageField(default=' ', upload_to='images'),
            preserve_default=False,
        ),
    ]