# Generated by Django 3.1.2 on 2021-01-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='status',
            field=models.CharField(choices=[('n', 'nowy'), ('b', 'Bestseller'), ('r', 'Przeczytane'), ('c', 'Nadchodzące')], default='n', max_length=1),
        ),
    ]
