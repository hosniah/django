# Generated by Django 3.2.8 on 2021-10-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='morceau',
            name='date_sortie',
            field=models.DateField(null=True),
        ),
    ]