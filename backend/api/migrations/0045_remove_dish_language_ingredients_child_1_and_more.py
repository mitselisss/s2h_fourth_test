# Generated by Django 4.2.2 on 2023-07-05 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_userprofilehistory_nuts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish_language',
            name='ingredients_child_1',
        ),
        migrations.RemoveField(
            model_name='dish_language',
            name='ingredients_child_2',
        ),
        migrations.RemoveField(
            model_name='dish_language',
            name='ingredients_child_3',
        ),
        migrations.RemoveField(
            model_name='dish_language',
            name='ingredients_child_4',
        ),
    ]
