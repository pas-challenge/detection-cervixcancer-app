# Generated by Django 4.1.3 on 2022-11-30 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("surveillance", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="docteur",
            options={
                "managed": True,
                "verbose_name": "Docteur",
                "verbose_name_plural": "Docteurs",
            },
        ),
    ]
