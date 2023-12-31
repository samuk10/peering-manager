# Generated by Django 3.2.11 on 2022-02-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peeringdb", "0022_internetexchange_sales")]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="info_traffic",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("0-20Mbps", "0-20Mbps"),
                    ("20-100Mbps", "20-100Mbps"),
                    ("100-1000Mbps", "100-1000Mbps"),
                    ("1-5Gbps", "1-5Gbps"),
                    ("5-10Gbps", "5-10Gbps"),
                    ("10-20Gbps", "10-20Gbps"),
                    ("20-50Gbps", "20-50Gbps"),
                    ("50-100Gbps", "50-100Gbps"),
                    ("100-200Gbps", "100-200Gbps"),
                    ("200-300Gbps", "200-300Gbps"),
                    ("300-500Gbps", "300-500Gbps"),
                    ("500-1000Gbps", "500-1000Gbps"),
                    ("1-5Tbps", "1-5Tbps"),
                    ("5-10Tbps", "5-10Tbps"),
                    ("10-20Tbps", "10-20Tbps"),
                    ("20-50Tbps", "20-50Tbps"),
                    ("50-100Tbps", "50-100Tbps"),
                    ("100+Tbps", "100+Tbps"),
                ],
                max_length=39,
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed"),
                    ("NSP", "NSP"),
                    ("Content", "Content"),
                    ("Cable/DSL/ISP", "Cable/DSL/ISP"),
                    ("Enterprise", "Enterprise"),
                    ("Educational/Research", "Educational/Research"),
                    ("Non-Profit", "Non-Profit"),
                    ("Route Server", "Route Server"),
                    ("Network Services", "Network Services"),
                    ("Route Collector", "Route Collector"),
                    ("Government", "Government"),
                ],
                default="",
                max_length=60,
            ),
        ),
    ]
