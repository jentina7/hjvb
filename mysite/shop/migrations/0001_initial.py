# Generated by Django 5.1.1 on 2024-09-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=32)),
                ("product_name_en", models.CharField(max_length=32, null=True)),
                ("product_name_ru", models.CharField(max_length=32, null=True)),
                ("product_name_ky", models.CharField(max_length=32, null=True)),
                ("product_name_kor", models.CharField(max_length=32, null=True)),
                ("description", models.TextField()),
                ("description_en", models.TextField(null=True)),
                ("description_ru", models.TextField(null=True)),
                ("description_ky", models.TextField(null=True)),
                ("description_kor", models.TextField(null=True)),
                ("completed", models.BooleanField(default=False)),
                ("created", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
