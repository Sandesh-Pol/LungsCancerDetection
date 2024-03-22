# Generated by Django 5.0.2 on 2024-02-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        max_length=10,
                    ),
                ),
                ("email", models.EmailField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("pincode", models.CharField(max_length=10)),
                (
                    "data_image",
                    models.FileField(
                        default=None, max_length=250, null=True, upload_to=""
                    ),
                ),
            ],
        ),
    ]