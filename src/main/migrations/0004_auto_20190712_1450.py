# Generated by Django 2.2.3 on 2019-07-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190712_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='firstGame',
            field=models.CharField(default='', max_length=120, null='True'),
        ),
        migrations.AlterField(
            model_name='game',
            name='secondGame',
            field=models.CharField(default='', max_length=120, null='True'),
        ),
    ]
