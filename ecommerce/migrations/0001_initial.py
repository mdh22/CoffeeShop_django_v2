# Generated by Django 4.2.4 on 2023-09-19 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('finish', models.BooleanField(blank=True, default=True, null=True)),
                ('city', models.CharField(default='', max_length=400)),
                ('zip_code', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('phone_no', models.CharField(default='', max_length=100)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=30)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cod'), ('CARD', 'Card')], default='COD', max_length=30)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Processing', max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('order_date',),
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False, unique=True)),
                ('quantity', models.PositiveIntegerField(default=1, null=True)),
                ('price_at_order', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product_name', models.CharField(blank=True, default='', max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderproducts', to='ecommerce.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
