# Generated by Django 4.1.9 on 2023-06-17 10:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0012_migrate_objectchanges"),
        ("utils", "0014_move_tags_to_extras"),
    ]

    operations = [migrations.DeleteModel(name="ObjectChange")]
