# Generated by Django 5.1 on 2024-09-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaticData', '0006_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('CreatedDt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['EventName'],
            },
        ),
    ]
