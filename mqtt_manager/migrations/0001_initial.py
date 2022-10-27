# Generated by Django 3.2.16 on 2022-10-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantsStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device', models.IntegerField()),
                ('date', models.IntegerField()),
                ('time', models.IntegerField()),
                ('light', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
            ],
        ),
    ]
