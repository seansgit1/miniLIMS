# Generated by Django 5.1 on 2024-09-12 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaticData', '0008_eventtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtest',
            name='UOM',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='StaticData.uom'),
            preserve_default=False,
        ),
    ]
