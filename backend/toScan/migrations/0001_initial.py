# Generated by Django 2.2.12 on 2020-04-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListToValidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBox', models.CharField(max_length=30)),
                ('estado', models.BigIntegerField(blank=True, null=True)),
                ('numeroCaja', models.CharField(blank=True, max_length=256, null=True)),
                ('pallet', models.CharField(blank=True, max_length=12, null=True)),
                ('idCliente', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
