# Generated by Django 4.1.5 on 2023-03-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_userdetails_gender_userdetails_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.PositiveIntegerField(default=1, max_length=15, unique=True),
        ),
    ]
