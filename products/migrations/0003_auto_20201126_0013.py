# Generated by Django 3.0.8 on 2020-11-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201110_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_preview',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
