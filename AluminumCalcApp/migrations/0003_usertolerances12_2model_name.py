# Generated by Django 5.1.1 on 2024-09-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AluminumCalcApp", "0002_tolerance12_2model_usertolerances12_2model"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertolerances12_2model",
            name="name",
            field=models.CharField(default="name", max_length=100),
            preserve_default=False,
        ),
    ]
