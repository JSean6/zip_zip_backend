# Generated by Django 5.0.6 on 2025-01-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0015_senterrands'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senterrands',
            name='clientPhoneNumber',
            field=models.IntegerField(),
        ),
    ]
