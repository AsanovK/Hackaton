# Generated by Django 4.0.5 on 2022-06-16 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('IN PROCESS', 'in process'), ('COMPLETED', 'completed'), ('DECLINED', 'declined')], default='in process', max_length=30)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_address', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='product.product')),
            ],
        ),
    ]
