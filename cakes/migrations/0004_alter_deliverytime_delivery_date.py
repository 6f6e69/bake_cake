# Generated by Django 4.2.3 on 2023-07-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0003_rename_inscription_order_text_order_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytime',
            name='delivery_date',
            field=models.DateField(verbose_name='Дата доставки'),
        ),
    ]
