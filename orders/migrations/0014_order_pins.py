# Generated by Django 3.0.3 on 2020-06-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0003_auto_20200527_0038'),
        ('orders', '0013_auto_20200503_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pins',
            field=models.ManyToManyField(to='pins.Pin'),
        ),
    ]