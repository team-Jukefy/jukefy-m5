# Generated by Django 4.1.5 on 2023-01-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="contact",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
