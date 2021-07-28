# Generated by Django 3.1.3 on 2021-07-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwash', '0007_auto_20210727_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='washplan',
            name='service',
            field=models.ManyToManyField(to='cwash.services'),
        ),
    ]