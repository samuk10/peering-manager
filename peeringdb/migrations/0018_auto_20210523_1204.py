# Generated by Django 3.2.3 on 2021-05-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peeringdb", "0017_auto_20210425_1229")]

    operations = [
        migrations.AddField(
            model_name="internetexchange",
            name="service_level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed Bis"),
                    ("Best Effort (no SLA)", "Best Effort"),
                    ("Normal Business Hours", "Normal Business Hours"),
                    ("24/7 Support", "Support 24 7"),
                ],
                default="",
                max_length=60,
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="terms",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed Bis"),
                    ("No Commercial Terms", "No Commercial Terms"),
                    ("Bundled With Other Services", "Bundled With Other Services"),
                    ("Non-recurring Fees Only", "Non Recurring Fees Only"),
                    ("Recurring Fees", "Recurring Fees"),
                ],
                default="",
                max_length=60,
            ),
        ),
    ]
