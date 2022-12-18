# Generated by Django 4.1.4 on 2022-12-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=50)),
                ("precio", models.IntegerField()),
                ("url_imagen", models.URLField(max_length=300)),
                ("url_origen", models.URLField(max_length=300)),
                ("direccion_proveedor", models.JSONField()),
                ("vistas", models.IntegerField(default=0)),
                ("estado", models.BooleanField(default=True)),
            ],
        ),
    ]