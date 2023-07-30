# Generated by Django 4.2.3 on 2023-07-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0002_ingredientcategory_alter_cake_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='inscription',
            new_name='text',
        ),
        migrations.AddField(
            model_name='order',
            name='contact_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Контактное лицо'),
        ),
        migrations.AddField(
            model_name='order',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Контактный телефон'),
        ),
        migrations.AlterField(
            model_name='deliverytime',
            name='delivery_status',
            field=models.CharField(choices=[('initial', 'План'), ('changed', 'Корректировка'), ('delivered', 'Факт')], max_length=40, verbose_name='Статус доставки'),
        ),
    ]
