# Generated by Django 4.1.7 on 2023-04-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commun', '0016_rename_nom_agenda_nom_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
