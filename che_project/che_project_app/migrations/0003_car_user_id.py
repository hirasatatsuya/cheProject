# Generated by Django 4.2.4 on 2023-08-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("che_project_app", "0002_car_weekday"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="user_id",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="che_project_app.user",
            ),
        ),
    ]