# Generated by Django 5.0.2 on 2024-02-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0007_alter_invoice_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]