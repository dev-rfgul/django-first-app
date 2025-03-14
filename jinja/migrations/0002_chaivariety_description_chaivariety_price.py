# Generated by Django 5.1.6 on 2025-03-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivariety',
            name='description',
            field=models.TextField(default='This is a chai variety'),
        ),
        migrations.AddField(
            model_name='chaivariety',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
