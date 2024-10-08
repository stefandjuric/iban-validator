# Generated by Django 4.2.15 on 2024-09-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iban_validator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestedIban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iban', models.CharField(max_length=34)),
                ('is_valid', models.BooleanField()),
                ('suggested_iban', models.CharField(max_length=34)),
            ],
        ),
    ]
