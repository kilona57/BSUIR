# Generated by Django 5.0 on 2023-12-18 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_budget_income_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='WithAgeAndMale',
        ),
        migrations.DeleteModel(
            name='WithDate',
        ),
        migrations.DeleteModel(
            name='WithPatient',
        ),
    ]
