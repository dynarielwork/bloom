# Generated by Django 3.0.10 on 2021-02-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20200927_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_vendor',
            field=models.BooleanField(default=True),
        ),
    ]