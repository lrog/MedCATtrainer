# Generated by Django 2.2 on 2019-05-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0007_auto_20190510_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usecase',
            name='cntx_tokens',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='cuis',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='other',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='tokens',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='tuis',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='usecase',
            name='type',
            field=models.CharField(blank=True, default='all', max_length=50),
        ),
    ]
