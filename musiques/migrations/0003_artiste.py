# Generated by Django 3.2.8 on 2021-10-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiques', '0002_morceau_date_sortie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
            ],
        ),
    ]
