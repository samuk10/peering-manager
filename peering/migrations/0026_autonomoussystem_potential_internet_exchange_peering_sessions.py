# Generated by Django 2.1.4 on 2018-12-31 23:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0025_auto_20181212_2322")]

    operations = [
        migrations.AddField(
            model_name="autonomoussystem",
            name="potential_internet_exchange_peering_sessions",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.GenericIPAddressField(),
                blank=True,
                default=list,
                size=None,
            ),
        )
    ]
