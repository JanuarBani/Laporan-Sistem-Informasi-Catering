# Generated by Django 5.1.1 on 2024-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catering1', '0019_remove_cateringmenu_stok_cateringmenu_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cateringmenu',
            name='img',
            field=models.ImageField(upload_to='static/myapp/img/'),
        ),
    ]
