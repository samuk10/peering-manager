# Generated by Django 3.1.3 on 2020-12-08 17:56

import django.db.models.deletion
import netfields.fields
from django.db import migrations, models

import peering.fields
import peeringdb.models
import utils.validators


class Migration(migrations.Migration):
    dependencies = [
        ("peering", "0065_auto_20201025_2137"),
        ("peeringdb", "0013_auto_20201207_2233"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.DeleteModel(
            name="PeerRecord",
        ),
        migrations.DeleteModel(
            name="Prefix",
        ),
        migrations.CreateModel(
            name="Facility",
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
                ("address1", models.CharField(blank=True, max_length=255)),
                ("address2", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(blank=True, max_length=255)),
                ("state", models.CharField(blank=True, max_length=255)),
                ("zipcode", models.CharField(blank=True, max_length=48)),
                ("country", models.CharField(blank=True, max_length=7)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("website", peeringdb.models.URLField(blank=True, max_length=255)),
                ("clli", models.CharField(blank=True, max_length=18)),
                ("rencode", models.CharField(blank=True, max_length=18)),
                ("npanxx", models.CharField(blank=True, max_length=21)),
                ("tech_email", models.EmailField(blank=True, max_length=254)),
                ("tech_phone", models.CharField(blank=True, max_length=192)),
                ("sales_email", models.EmailField(blank=True, max_length=254)),
                ("sales_phone", models.CharField(blank=True, max_length=192)),
                ("notes", models.TextField(blank=True)),
            ],
            options={
                "verbose_name_plural": "facilities",
            },
        ),
        migrations.CreateModel(
            name="InternetExchange",
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
                ("name", models.CharField(max_length=64, unique=True)),
                ("name_long", models.CharField(blank=True, max_length=254)),
                ("city", models.CharField(max_length=192)),
                ("country", models.CharField(blank=True, max_length=7)),
                ("notes", models.TextField(blank=True)),
                (
                    "region_continent",
                    models.CharField(
                        choices=[
                            ("North America", "North America"),
                            ("Asia Pacific", "Asia Pacific"),
                            ("Europe", "Europe"),
                            ("South America", "South America"),
                            ("Africa", "Africa"),
                            ("Australia", "Australia"),
                            ("Middle East", "Middle East"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "media",
                    models.CharField(
                        choices=[
                            ("Ethernet", "Ethernet"),
                            ("ATM", "Atm"),
                            ("Multiple", "Multiple"),
                        ],
                        max_length=128,
                    ),
                ),
                ("proto_unicast", models.BooleanField(default=False)),
                ("proto_multicast", models.BooleanField(default=False)),
                ("proto_ipv6", models.BooleanField(default=False)),
                ("website", peeringdb.models.URLField(blank=True, max_length=255)),
                ("url_stats", peeringdb.models.URLField(blank=True, max_length=255)),
                ("tech_email", models.EmailField(blank=True, max_length=254)),
                ("tech_phone", models.CharField(blank=True, max_length=192)),
                ("policy_email", models.EmailField(blank=True, max_length=254)),
                ("policy_phone", models.CharField(blank=True, max_length=192)),
                ("ixf_net_count", models.IntegerField(default=0)),
                ("ixf_last_import", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Internet Exchange",
                "verbose_name_plural": "Internet Exchanges",
            },
        ),
        migrations.CreateModel(
            name="InternetExchangeFacility",
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
                (
                    "fac",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ixfac_set",
                        to="peeringdb.facility",
                        verbose_name="Facility",
                    ),
                ),
                (
                    "ix",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ixfac_set",
                        to="peeringdb.internetexchange",
                        verbose_name="Internet Exchange",
                    ),
                ),
            ],
            options={
                "verbose_name": "Internet Exchange facility",
                "verbose_name_plural": "Internet Exchange facilities",
                "unique_together": {("ix", "fac")},
            },
        ),
        migrations.CreateModel(
            name="IXLan",
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
                ("name", models.CharField(blank=True, max_length=255)),
                ("descr", models.TextField(blank=True)),
                ("mtu", models.PositiveIntegerField(blank=True, null=True)),
                ("vlan", models.PositiveIntegerField(blank=True, null=True)),
                ("dot1q_support", models.BooleanField(default=False)),
                (
                    "rs_asn",
                    peering.fields.ASNField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="Route Server ASN",
                    ),
                ),
                (
                    "arp_sponge",
                    netfields.fields.MACAddressField(
                        blank=True,
                        null=True,
                        unique=True,
                        verbose_name="ARP sponging MAC",
                    ),
                ),
                (
                    "ixf_ixp_member_list_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="IX-F Member Export URL"
                    ),
                ),
                (
                    "ixf_ixp_member_list_url_visible",
                    models.CharField(
                        choices=[
                            ("Private", "Private"),
                            ("Users", "Users"),
                            ("Public", "Public"),
                        ],
                        default="Private",
                        max_length=64,
                        verbose_name="IX-F Member Export URL Visibility",
                    ),
                ),
                (
                    "ix",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ixlan_set",
                        to="peeringdb.internetexchange",
                        verbose_name="Internet Exchange",
                    ),
                ),
            ],
            options={
                "verbose_name": "Internet Exchange LAN",
                "verbose_name_plural": "Internet Exchange LANs",
            },
        ),
        migrations.CreateModel(
            name="IXLanPrefix",
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
                ("notes", models.CharField(blank=True, max_length=255)),
                (
                    "protocol",
                    models.CharField(
                        choices=[("IPv4", "Ipv4"), ("IPv6", "Ipv6")], max_length=64
                    ),
                ),
                (
                    "prefix",
                    netfields.fields.CidrAddressField(max_length=43, unique=True),
                ),
                ("in_dfz", models.BooleanField(default=False)),
                (
                    "ixlan",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ixpfx_set",
                        to="peeringdb.ixlan",
                        verbose_name="Internet Exchange LAN",
                    ),
                ),
            ],
            options={
                "verbose_name": "Internet Exchange LAN prefix",
                "verbose_name_plural": "Internet Exchange LAN prefixes",
            },
        ),
        migrations.CreateModel(
            name="NetworkContact",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Abuse", "Abuse"),
                            ("Maintenance", "Maintenance"),
                            ("Policy", "Policy"),
                            ("Technical", "Technical"),
                            ("NOC", "NOC"),
                            ("Public Relations", "Public Relations"),
                            ("Sales", "Sales"),
                        ],
                        max_length=27,
                    ),
                ),
                (
                    "visible",
                    models.CharField(
                        choices=[
                            ("Private", "Private"),
                            ("Users", "Users"),
                            ("Public", "Public"),
                        ],
                        default="Public",
                        max_length=64,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("url", peeringdb.models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="NetworkFacility",
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
                (
                    "local_asn",
                    peering.fields.ASNField(
                        blank=True, null=True, verbose_name="Local ASN"
                    ),
                ),
                ("avail_sonet", models.BooleanField(default=False)),
                ("avail_ethernet", models.BooleanField(default=False)),
                ("avail_atm", models.BooleanField(default=False)),
                (
                    "fac",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="netfac_set",
                        to="peeringdb.facility",
                        verbose_name="Facility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Network Facility",
                "verbose_name_plural": "Network Facilities",
            },
        ),
        migrations.CreateModel(
            name="Organization",
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
                ("address1", models.CharField(blank=True, max_length=255)),
                ("address2", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(blank=True, max_length=255)),
                ("state", models.CharField(blank=True, max_length=255)),
                ("zipcode", models.CharField(blank=True, max_length=48)),
                ("country", models.CharField(blank=True, max_length=7)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("website", peeringdb.models.URLField(blank=True, max_length=255)),
                ("notes", models.TextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="network",
            options={},
        ),
        migrations.AlterModelOptions(
            name="networkixlan",
            options={
                "verbose_name": "Public Peering Exchange Point",
                "verbose_name_plural": "Public Peering Exchange Points",
            },
        ),
        migrations.RenameField(
            model_name="synchronization",
            old_name="added",
            new_name="created",
        ),
        migrations.RemoveField(
            model_name="networkixlan",
            name="ix_id",
        ),
        migrations.RemoveField(
            model_name="networkixlan",
            name="ixlan_id",
        ),
        migrations.RemoveField(
            model_name="networkixlan",
            name="name",
        ),
        migrations.AddField(
            model_name="network",
            name="aka",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Also Known As"
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_ipv6",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="network",
            name="info_multicast",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="network",
            name="info_never_via_route_servers",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if this network will announce its routes via route servers or not",
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_ratio",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed Bis"),
                    ("Heavy Outbound", "Heavy Outbound"),
                    ("Mostly Outbound", "Mostly Outbound"),
                    ("Balanced", "Balanced"),
                    ("Mostly Inbound", "Mostly Inbound"),
                    ("Heavy Inbound", "Heavy Inbound"),
                ],
                default="",
                max_length=45,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_scope",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed Bis"),
                    ("Regional", "Regional"),
                    ("North America", "North America"),
                    ("Asia Pacific", "Asia Pacific"),
                    ("Europe", "Europe"),
                    ("South America", "South America"),
                    ("Africa", "Africa"),
                    ("Australia", "Australia"),
                    ("Middle East", "Middle East"),
                    ("Global", "Global"),
                ],
                default="",
                max_length=39,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_traffic",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("0-20Mbps", "Mbps 20"),
                    ("20-100Mbps", "Mbps 100"),
                    ("100-1000Mbps", "Gbps 1"),
                    ("1-5Gbps", "Gbps 5"),
                    ("5-10Gbps", "Gbps 10"),
                    ("10-20Gbps", "Gbps 20"),
                    ("20-50Gbps", "Gbps 50"),
                    ("50-100Gbps", "Gbps 100"),
                    ("100-200Gbps", "Gbps 200"),
                    ("200-300Gbps", "Gbps 300"),
                    ("300-500Gbps", "Gbps 500"),
                    ("500-1000Gbps", "Tbps 1"),
                    ("1-5Tbps", "Tbps 5"),
                    ("5-10Tbps", "Tbps 10"),
                    ("10-20Tbps", "Tbps 20"),
                    ("20-50Tbps", "Tbps 50"),
                    ("50-100Tbps", "Tbps 100"),
                    ("100+Tbps", "Tbps 100 Plus"),
                ],
                max_length=39,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed Bis"),
                    ("NSP", "Nsp"),
                    ("Content", "Content"),
                    ("Cable/DSL/ISP", "Cable Dsl Isp"),
                    ("Enterprise", "Entreprise"),
                    ("Educational/Research", "Educational Research"),
                    ("Non-Profit", "Non Profit"),
                    ("Route Server", "Route Server"),
                    ("Network Services", "Network Services"),
                    ("Route Collector", "Route Collector"),
                    ("Government", "Government"),
                ],
                default="",
                max_length=60,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="info_unicast",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="network",
            name="looking_glass",
            field=peeringdb.models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="network",
            name="notes",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="network",
            name="notes_private",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="network",
            name="policy_contracts",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Not Required", "Not Required"),
                    ("Private Only", "Private Only"),
                    ("Required", "Required"),
                ],
                max_length=36,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="policy_general",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Open", "Open"),
                    ("Selective", "Selective"),
                    ("Restrictive", "Restrictive"),
                    ("No", "No"),
                ],
                max_length=72,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="policy_locations",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Not Required", "Not Required"),
                    ("Preferred", "Preferred"),
                    ("Required - US", "Required Us"),
                    ("Required - EU", "Required Eu"),
                    ("Required - International", "Required Int"),
                ],
                max_length=72,
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="policy_ratio",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="network",
            name="policy_url",
            field=peeringdb.models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="network",
            name="route_server",
            field=peeringdb.models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="network",
            name="website",
            field=peeringdb.models.URLField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="networkixlan",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netixlan_set",
                to="peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AddField(
            model_name="networkixlan",
            name="notes",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="networkixlan",
            name="operational",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="networkixlan",
            name="speed",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="network",
            name="asn",
            field=peering.fields.ASNField(unique=True, verbose_name="ASN"),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes4",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended maximum number of IPv4 routes/prefixes to be configured on peering sessions for this ASN",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes6",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Recommended maximum number of IPv6 routes/prefixes to be configured on peering sessions for this ASN",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="irr_as_set",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Reference to an AS-SET or ROUTE-SET in Internet Routing Registry (IRR)",
                max_length=255,
                verbose_name="IRR AS-SET/ROUTE-SET",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="network",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="asn",
            field=peering.fields.ASNField(verbose_name="ASN"),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="ipaddr4",
            field=netfields.fields.InetAddressField(
                blank=True,
                max_length=39,
                null=True,
                validators=[utils.validators.AddressFamilyValidator(4)],
                verbose_name="IPv4",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="ipaddr6",
            field=netfields.fields.InetAddressField(
                blank=True,
                max_length=39,
                null=True,
                validators=[utils.validators.AddressFamilyValidator(6)],
                verbose_name="IPv6",
            ),
        ),
        migrations.AddField(
            model_name="networkfacility",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netfac_set",
                to="peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AddField(
            model_name="networkcontact",
            name="net",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poc_set",
                to="peeringdb.network",
                verbose_name="Network",
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ix_set",
                to="peeringdb.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fac_set",
                to="peeringdb.organization",
                verbose_name="Organization",
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="org",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="net_set",
                to="peeringdb.organization",
                verbose_name="Organization",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="networkixlan",
            name="ixlan",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="netixlan_set",
                to="peeringdb.ixlan",
                verbose_name="Internet Exchange LAN",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="networkfacility",
            unique_together={("net", "fac", "local_asn")},
        ),
    ]
