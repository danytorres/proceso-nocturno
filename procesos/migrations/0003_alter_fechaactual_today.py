# Generated by Django 4.1.1 on 2022-09-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0002_fechaactual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechaactual',
            name='today',
            field=models.DateTimeField(),
        ),
    ]
