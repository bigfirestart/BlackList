# Generated by Django 2.1.2 on 2019-03-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlackList', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='anger',
            new_name='anger_procent',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='reason',
            field=models.CharField(max_length=200),
        ),
    ]
