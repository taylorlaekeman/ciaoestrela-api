from django.db import migrations


ORDER_TYPES = [
    { 'id': 1, 'name': 'custom card' },
]

def seed_order_type(apps, schema_editor):
    OrderType = apps.get_model('orders', 'OrderType')
    for order_type in ORDER_TYPES:
        OrderType.objects.create(**order_type)


class Migration(migrations.Migration):
    dependencies = [('orders', '0001_initial')]
    operations = [migrations.RunPython(seed_order_type)]
