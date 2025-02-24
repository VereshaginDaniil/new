from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукция'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AddConstraint(
            model_name='stockproduct',
            constraint=models.UniqueConstraint(fields=('stock', 'product'), name='unique stock_product'),
        ),
    ]
