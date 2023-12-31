# Generated by Django 4.0.7 on 2022-10-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("extras", "0006_exporttemplate")]

    operations = [
        migrations.AddField(
            model_name="ixapi",
            name="access_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ixapi",
            name="access_token_expiration",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ixapi",
            name="refresh_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ixapi",
            name="refresh_token_expiration",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
