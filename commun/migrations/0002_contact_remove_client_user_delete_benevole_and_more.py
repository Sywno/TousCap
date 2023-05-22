# Generated by Django 4.1.7 on 2023-03-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_benevole', models.BooleanField(default=True)),
                ('is_client', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.DeleteModel(
            name='Benevole',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]