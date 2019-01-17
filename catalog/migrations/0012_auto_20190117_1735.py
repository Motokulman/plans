# Generated by Django 2.1.4 on 2019-01-17 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20190117_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular form factor across whole catalog', primary_key=True, serialize=False),
        ),
    ]
