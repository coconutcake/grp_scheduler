# Generated by Django 3.1.3 on 2021-07-02 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Konto użytkownika', 'verbose_name_plural': 'Konta użytkowników'},
        ),
    ]
