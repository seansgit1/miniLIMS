# Generated by Django 5.1 on 2024-08-30 07:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Samples', '0001_initial'),
        ('StaticData', '0006_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='MaterialID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='StaticData.material'),
        ),
        migrations.AddField(
            model_name='sample',
            name='SampleDt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='StatusID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StaticData.status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='UserText1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
