# Generated by Django 4.0 on 2022-08-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auditlog", "0010_alter_logentry_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="serialized_data",
            field=models.JSONField(null=True),
        ),
    ]
