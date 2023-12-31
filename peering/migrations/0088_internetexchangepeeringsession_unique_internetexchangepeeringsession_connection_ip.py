# Generated by Django 3.2.11 on 2022-02-03 00:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0087_move_poll_bgp_sessions_to_router")]

    operations = [
        migrations.AddConstraint(
            model_name="internetexchangepeeringsession",
            constraint=models.UniqueConstraint(
                fields=("ixp_connection", "ip_address"),
                name="unique_internetexchangepeeringsession_connection_ip",
            ),
        ),
    ]
