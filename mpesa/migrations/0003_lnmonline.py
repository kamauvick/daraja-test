# Generated by Django 3.0.2 on 2020-01-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0002_auto_20200124_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]