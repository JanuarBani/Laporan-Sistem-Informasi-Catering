# Generated by Django 5.1.1 on 2024-10-29 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0007_alter_cateringmenu_idkate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cateringmenu',
            name='idKate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='catering1.categorimenu', verbose_name='idKate'),
        ),
    ]
