# Generated by Django 3.1.7 on 2021-03-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0310_jsonfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="customer_showcase_policy",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
