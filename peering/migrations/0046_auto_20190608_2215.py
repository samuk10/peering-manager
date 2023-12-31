# Generated by Django 2.2.2 on 2019-06-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0045_auto_20190514_2308")]

    operations = [
        migrations.AlterField(
            model_name="router",
            name="encrypt_passwords",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Try to encrypt passwords for peering sessions",
            ),
        )
    ]
