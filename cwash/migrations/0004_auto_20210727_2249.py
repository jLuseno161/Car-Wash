# Generated by Django 3.1.3 on 2021-07-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwash', '0003_auto_20210727_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]