# Generated by Django 3.0.8 on 2020-07-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]