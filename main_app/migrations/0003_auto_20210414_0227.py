# Generated by Django 3.1.7 on 2021-04-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210413_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
