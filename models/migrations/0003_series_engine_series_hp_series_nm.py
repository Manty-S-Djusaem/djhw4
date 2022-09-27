# Generated by Django 4.1.1 on 2022-09-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='engine',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='hp',
            field=models.IntegerField(blank=True, null=True, verbose_name='лошадиные силы'),
        ),
        migrations.AddField(
            model_name='series',
            name='nm',
            field=models.IntegerField(blank=True, null=True, verbose_name='мощность'),
        ),
    ]
