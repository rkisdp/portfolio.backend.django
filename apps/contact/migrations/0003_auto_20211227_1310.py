# Generated by Django 3.2.7 on 2021-12-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contact", "0002_auto_20211006_2357")]

    operations = [
        migrations.AddField(
            model_name="contactform",
            name="extra_data",
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name="Extra Data"),
        ),
        migrations.AddField(
            model_name="sociallink",
            name="extra_data",
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name="Extra Data"),
        ),
    ]