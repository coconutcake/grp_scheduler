# Generated by Django 3.1.3 on 2021-07-02 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20210630_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.group', verbose_name='Grupa'),
        ),
    ]