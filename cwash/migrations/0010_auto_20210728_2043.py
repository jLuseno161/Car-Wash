# Generated by Django 3.1.3 on 2021-07-28 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwash', '0009_auto_20210727_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='booking',
            name='plan',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cwash.washplan'),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle_type',
            field=models.CharField(choices=[('', 'Choose Vehicle Type'), ('Regular Car', 'Regular Car'), ('Medium Car', 'Medium Car'), ('Compact Suv', 'Compact Suv'), ('Mini Van', 'Mini Van'), ('Pickup Truck', 'Pickup Truck'), ('Cargo Truck', 'Cargo Truck')], default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='appointment_date',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timeframe',
            field=models.CharField(choices=[('', 'Choose Time Frame'), ('Morning', 'Morning'), ('Evening', 'Evening'), ('Afternoon', 'Afternoon')], default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='washplan',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, related_name='services', to='cwash.services'),
        ),
    ]
