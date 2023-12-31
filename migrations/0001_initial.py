# Generated by Django 4.2.3 on 2023-07-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField(auto_created=True)),
                ('nom', models.CharField(max_length=150)),
                ('prix', models.IntegerField(default=0)),
                ('categorie', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Habit',
                'verbose_name_plural': 'Habits',
                'ordering': ['-Date'],
            },
        ),
    ]
