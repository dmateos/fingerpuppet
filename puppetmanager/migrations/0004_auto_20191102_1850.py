# Generated by Django 2.1.11 on 2019-11-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("puppetmanager", "0003_auto_20191102_1846")]

    operations = [
        migrations.AlterField(
            model_name="node",
            name="classifications",
            field=models.ManyToManyField(blank=True, to="puppetmanager.Classification"),
        )
    ]
