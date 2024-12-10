# Generated by Django 5.1.1 on 2024-10-29 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0011_alter_detailpemesanan_idpemesanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailpemesanan',
            name='jumlahItemMenu',
            field=models.PositiveIntegerField(verbose_name='Jumlah Item Menu'),
        ),
        migrations.AlterField(
            model_name='detailpemesananacara',
            name='idPemesanan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detailAcara', to='catering1.pemesananacara', verbose_name='ID Pemesanan'),
        ),
    ]