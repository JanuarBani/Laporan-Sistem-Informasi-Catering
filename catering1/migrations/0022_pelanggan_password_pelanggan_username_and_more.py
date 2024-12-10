# Generated by Django 5.1.1 on 2024-11-19 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0021_alter_pemesananpelanggan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelanggan',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='acara',
            name='idKategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acara', to='catering1.categori', verbose_name='idKategori'),
        ),
    ]