# Generated by Django 3.2.8 on 2021-11-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp_items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
