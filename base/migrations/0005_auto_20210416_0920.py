# Generated by Django 3.1.3 on 2021-04-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210416_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='o1_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o2_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o3_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o4_votes',
            field=models.IntegerField(default=0),
        ),
    ]
