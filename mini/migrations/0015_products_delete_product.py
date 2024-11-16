# FILE: 0015_products_delete_product.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0014_previous_migration'),
    ]

    operations = [
        # If the products model is deleted, comment out or remove the deletion operation
        # migrations.DeleteModel(
        #     name='products',
        # ),
    ]