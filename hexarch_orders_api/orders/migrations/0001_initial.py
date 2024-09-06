# Generated by Django 5.0.4 on 2024-09-06 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.itemmodel')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price_without_tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total_price_with_tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(through='orders.OrderItem', to='items.itemmodel')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ordermodel'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('order', 'item')},
        ),
    ]
