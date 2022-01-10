# Generated by Django 3.2.11 on 2022-01-07 22:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("peering", "0082_move_autonomoussystem_contacts")]

    database_operations = [migrations.AlterModelTable("Email", "messaging_email")]
    state_operations = [migrations.DeleteModel("Email")]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations, state_operations=state_operations
        )
    ]