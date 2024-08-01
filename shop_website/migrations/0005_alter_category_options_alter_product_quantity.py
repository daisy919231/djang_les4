# Generated by Django 5.0.7 on 2024-08-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_website', '0004_alter_comment_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
