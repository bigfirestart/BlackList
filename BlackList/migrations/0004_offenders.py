# Generated by Django 2.1.2 on 2019-03-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlackList', '0003_auto_20190307_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offenders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
            ],
        ),
    ]
