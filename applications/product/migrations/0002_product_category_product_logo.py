# Generated by Django 4.0.5 on 2022-06-15 15:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='category.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='logo',
            field=models.ImageField(blank=True, default='images/2-500x500_iwW2IIp.jpeg', null=True, upload_to='images'),
        ),
    ]
