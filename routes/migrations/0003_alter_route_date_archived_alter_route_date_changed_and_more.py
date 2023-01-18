# Generated by Django 4.0.3 on 2022-05-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("routes", "0002_rename_routes_route"),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="date_archived",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="route",
            name="date_changed",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="route",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
