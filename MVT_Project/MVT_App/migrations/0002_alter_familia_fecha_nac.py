# Generated by Django 4.0.6 on 2022-07-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fecha_nac',
            field=models.CharField(max_length=50),
        ),
    ]
