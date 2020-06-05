# Generated by Django 3.0.3 on 2020-06-02 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_cards', '0002_auto_20200602_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='customcard',
            name='paper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='custom_cards.PaperType'),
        ),
    ]