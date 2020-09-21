# Generated by Django 3.0.8 on 2020-07-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentLocations',
            fields=[
                ('id', models.IntegerField(primary_key='True', serialize=False)),
                ('name', models.TextField()),
                ('Address', models.TextField()),
                ('city', models.TextField()),
                ('zipcode', models.IntegerField()),
                ('state', models.TextField()),
            ],
        ),
    ]
