# Generated by Django 3.1.3 on 2021-06-30 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_group_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.group', verbose_name='Grupa'),
        ),
    ]
