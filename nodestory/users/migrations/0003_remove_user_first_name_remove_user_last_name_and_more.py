# Generated by Django 5.1.3 on 2024-12-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_nickname_alter_user_date_joined_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
        migrations.AlterField(
            model_name="user",
            name="likes_total",
            field=models.IntegerField(default=0),
        ),
    ]
