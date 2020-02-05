from django.db import migrations


PAPER_TYPES = [
    { 'id': 1, 'name': '4" x 5.5" white' },
    { 'id': 2, 'name': '4" x 5.5" ivory' },
    { 'id': 3, 'name': '4" x 5.5" brown' },
    { 'id': 4, 'name': '5" x 6.5" white' },
]

def seed_paper_type(apps, schema_editor):
    PaperType = apps.get_model('orders', 'PaperType')
    for paper_type in PAPER_TYPES:
        PaperType.objects.create(**paper_type)


class Migration(migrations.Migration):
    dependencies = [('orders', '0004_auto_20200205_2243')]
    operations = [migrations.RunPython(seed_paper_type)]
