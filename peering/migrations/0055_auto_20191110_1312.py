# Generated by Django 2.2.6 on 2019-11-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0054_auto_20191031_2241")]

    operations = [
        migrations.AddField(
            model_name="directpeeringsession",
            name="encrypted_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="encrypted_password",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
