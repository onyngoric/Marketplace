# Generated by Django 4.1.5 on 2023-12-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_remove_ad_media_alter_ad_category_alter_ad_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimages',
            name='media',
            field=models.FileField(upload_to='static/Adimages/'),
        ),
    ]