# Generated by Django 3.0.8 on 2020-11-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0002_auto_20201122_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_description',
            field=models.TextField(blank=True, default="Please provide a quick description of your game's quality", max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='sealed',
            field=models.BooleanField(help_text="Only tick this box if your game is still contained in it's original wrapping", null=True),
        ),
    ]