# Generated by Django 4.0.5 on 2022-07-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='otp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
