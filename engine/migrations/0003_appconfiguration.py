# Generated by Django 2.1.7 on 2019-02-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("engine", "0002_account")]

    operations = [
        migrations.CreateModel(
            name="AppConfiguration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("aws_dns_auth", models.TextField(default="")),
            ],
            options={"get_latest_by": "created"},
        )
    ]
