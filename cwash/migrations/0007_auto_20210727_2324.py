# Generated by Django 3.1.3 on 2021-07-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwash', '0006_auto_20210727_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='washplan',
            name='airfreshner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='coat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='dashboard',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='hdry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='hwash',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='rainx',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='sealer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='tdress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='vacuum',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='vinyl',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='window',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='wshine',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]