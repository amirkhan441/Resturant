# Generated by Django 5.2 on 2025-04-10 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp2', '0004_alter_item_item_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Items',
        ),
    ]
