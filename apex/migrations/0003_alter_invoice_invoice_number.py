# Generated by Django 3.2.7 on 2021-11-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0002_alter_invoice_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]