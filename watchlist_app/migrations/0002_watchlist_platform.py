# Generated by Django 5.0.4 on 2024-04-27 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="watchlist_app.streamplatform",
            ),
            preserve_default=False,
        ),
    ]