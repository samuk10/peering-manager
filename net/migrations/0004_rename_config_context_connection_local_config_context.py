# Generated by Django 4.0.4 on 2022-06-10 20:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("net", "0003_connection_config_context")]

    operations = [
        migrations.RenameField(
            model_name="connection",
            old_name="config_context",
            new_name="local_context_data",
        ),
    ]
