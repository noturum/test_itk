# Generated by Django 5.1.3 on 2024-12-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ne', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('gsm', models.BooleanField()),
                ('umts', models.BooleanField()),
                ('lte', models.BooleanField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
