# Generated by Django 2.1.7 on 2019-03-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0032_auto_20190302_1415")]

    operations = [
        migrations.AddField(
            model_name="router",
            name="encrypt_passwords",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="Try to encrypt passwords in router's configuration",
            ),
        )
    ]
