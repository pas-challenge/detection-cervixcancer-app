# Generated by Django 4.1.3 on 2022-11-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveillance", "0003_remove_docteur_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diagnostic",
            name="prediction",
            field=models.IntegerField(),
        ),
    ]