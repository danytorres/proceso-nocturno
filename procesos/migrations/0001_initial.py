# Generated by Django 4.1.1 on 2022-09-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tabla_0_1",
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
                ("id_job", models.CharField(max_length=30)),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tabla_1_2",
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
                ("id_job", models.CharField(max_length=30)),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tabla_23_0",
            fields=[
                (
                    "id_job",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tabla_2_3",
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
                ("id_job", models.CharField(max_length=30)),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tabla_3_4",
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
                ("id_job", models.CharField(max_length=30)),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Tabla_4_5",
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
                ("id_job", models.CharField(max_length=30)),
                ("job", models.CharField(max_length=30)),
                ("carpeta", models.CharField(max_length=30)),
                ("proceso", models.CharField(max_length=30)),
                ("tipo", models.CharField(max_length=30)),
                ("com", models.CharField(max_length=30)),
                ("secuencia", models.CharField(max_length=30)),
                ("hora", models.CharField(max_length=30)),
            ],
        ),
    ]
