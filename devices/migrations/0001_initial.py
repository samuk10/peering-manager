# Generated by Django 3.1.6 on 2021-02-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    def add_default_napalm_platforms(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        Platform = apps.get_model("devices", "Platform")

        platforms = [
            Platform(
                name="Arista EOS",
                slug="arista-eos",
                napalm_driver="eos",
                password_algorithm="cisco-type7",
            ),
            Platform(
                name="Juniper Junos",
                slug="juniper-junos",
                napalm_driver="junos",
                password_algorithm="juniper-type9",
            ),
            Platform(
                name="Cisco IOS-XR",
                slug="cisco-iosxr",
                napalm_driver="iosxr",
                password_algorithm="cisco-type7",
            ),
            Platform(
                name="Cisco NX-OS",
                slug="cisco-nxos",
                napalm_driver="nxos",
                password_algorithm="cisco-type7",
            ),
            Platform(
                name="Cisco IOS",
                slug="cisco-ios",
                napalm_driver="ios",
                password_algorithm="cisco-type7",
            ),
            Platform(
                name="Nokia SR OS",
                slug="nokia-sros",
                napalm_driver="sros",
                password_algorithm="nokia-cus-aes256",
            ),
        ]
        Platform.objects.using(db_alias).bulk_create(platforms)

    operations = [
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Friendly unique shorthand used for URL and config",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "napalm_driver",
                    models.CharField(
                        blank=True,
                        help_text="The name of the NAPALM driver to use when interacting with devices",
                        max_length=50,
                        verbose_name="NAPALM driver",
                    ),
                ),
                (
                    "napalm_args",
                    models.JSONField(
                        blank=True,
                        help_text="Additional arguments to pass when initiating the NAPALM driver (JSON format)",
                        null=True,
                        verbose_name="NAPALM arguments",
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "password_algorithm",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("cisco-type7", "Cisco Type 7"),
                            ("juniper-type9", "Juniper Type 9"),
                            ("nokia-cus-aes256", "Nokia custom AES256"),
                        ],
                        help_text="Algorithm to cipher password in configuration",
                        max_length=16,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.RunPython(add_default_napalm_platforms),
    ]
