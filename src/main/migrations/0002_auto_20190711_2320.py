# Generated by Django 2.2.3 on 2019-07-12 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='first_game',
            new_name='firstGame',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='min_rating',
            new_name='minRating',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='second_game',
            new_name='secondGame',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='third_game',
            new_name='thirdGame',
        ),
    ]
