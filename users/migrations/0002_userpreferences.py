# Generated by Django 3.0.6 on 2020-05-18 22:25

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import migrations, models


def create_userprefs(apps, schema_editor):
    """
    Create an empty UserPreferences instance for each existing User.
    """
    User = get_user_model()
    UserPreferences = apps.get_model("users", "UserPreferences")
    UserPreferences.objects.bulk_create(
        [UserPreferences(user_id=user.pk) for user in User.objects.all()]
    )


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPreferences",
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
                ("data", django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preferences",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Preferences",
                "verbose_name_plural": "User Preferences",
                "ordering": ["user"],
            },
        ),
        migrations.RunPython(
            code=create_userprefs, reverse_code=migrations.RunPython.noop
        ),
    ]
