# Generated by Django 4.1.5 on 2023-01-06 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(blank=True, default=True),
        ),
    ]