# Generated by Django 4.0 on 2021-12-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromdate', models.CharField(max_length=100)),
                ('todate', models.CharField(max_length=100)),
                ('noofguest', models.CharField(max_length=100)),
                ('typeofacc', models.CharField(max_length=100)),
            ],
        ),
    ]
