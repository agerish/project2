# Generated by Django 4.2.3 on 2023-07-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0012_dress_shop_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_provenant_de_la_page_de_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('suject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Message_provenant_de_la_page_de_contact',
                'verbose_name_plural': 'Message_provenant_de_la_page_de_contacts',
                'ordering': ['-Date'],
            },
        ),
    ]
