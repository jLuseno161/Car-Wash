# Generated by Django 3.1.3 on 2021-07-27 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cwash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Washplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('hwash', models.CharField(max_length=50)),
                ('hdry', models.CharField(max_length=50)),
                ('wshine', models.CharField(max_length=50)),
                ('tdress', models.CharField(max_length=50)),
                ('window', models.CharField(max_length=50)),
                ('sealer', models.CharField(max_length=50)),
                ('vacuum', models.CharField(max_length=50)),
                ('dashboard', models.CharField(max_length=50)),
                ('airfreshner', models.CharField(max_length=50)),
                ('coat', models.CharField(max_length=50)),
                ('vinyl', models.CharField(max_length=50)),
                ('rainx', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=30)),
                ('mobile', models.IntegerField(default=0)),
                ('appointment_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
