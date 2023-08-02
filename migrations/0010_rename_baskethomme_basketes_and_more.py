# Generated by Django 4.2.3 on 2023-07-27 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_rename_baskets_basket_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Baskethomme',
            new_name='Basketes',
        ),
        migrations.RenameModel(
            old_name='Basket',
            new_name='Basketsfemmes',
        ),
        migrations.RenameModel(
            old_name='Basketfemme',
            new_name='Basketshommes',
        ),
        migrations.AlterModelOptions(
            name='basketes',
            options={'ordering': ['-Date'], 'verbose_name': 'Baskete', 'verbose_name_plural': 'Basketes'},
        ),
        migrations.AlterModelOptions(
            name='basketsfemmes',
            options={'ordering': ['-Date'], 'verbose_name': 'Basketsfemme', 'verbose_name_plural': 'Basketsfemmes'},
        ),
        migrations.AlterModelOptions(
            name='basketshommes',
            options={'ordering': ['-Date'], 'verbose_name': 'Basketshomme', 'verbose_name_plural': 'Basketshommes'},
        ),
    ]
