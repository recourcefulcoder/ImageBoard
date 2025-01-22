# Generated by Django 5.1.3 on 2025-01-22 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0002_remove_closuretable_ancestor_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="closuretable",
            name="descendant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="parents",
                to="stories.storynode",
            ),
        ),
    ]
