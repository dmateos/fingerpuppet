# Generated by Django 2.1.11 on 2019-11-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("puppetmanager", "0004_auto_20191102_1850")]

    operations = [
        migrations.AddField(
            model_name="node",
            name="total_checkins",
            field=models.IntegerField(default=0),
        )
    ]
