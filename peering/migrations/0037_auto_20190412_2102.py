# Generated by Django 2.2 on 2019-04-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0036_auto_20190411_2209")]

    operations = [
        migrations.AddField(
            model_name="directpeeringsession",
            name="multihop_ttl",
            field=models.PositiveSmallIntegerField(
                blank=True,
                default=1,
                help_text="Used a value greater than 1 for BGP multihop sessions",
                verbose_name="Multihop TTL",
            ),
        ),
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="multihop_ttl",
            field=models.PositiveSmallIntegerField(
                blank=True,
                default=1,
                help_text="Used a value greater than 1 for BGP multihop sessions",
                verbose_name="Multihop TTL",
            ),
        ),
    ]
