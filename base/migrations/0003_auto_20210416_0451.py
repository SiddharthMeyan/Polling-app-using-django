# Generated by Django 3.1.3 on 2021-04-16 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210416_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='o1_votes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o2_votes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o3_votes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='o4_votes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='total_votes',
            field=models.IntegerField(blank=True),
        ),
    ]
