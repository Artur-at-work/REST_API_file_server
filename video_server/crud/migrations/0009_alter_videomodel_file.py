# Generated by Django 4.1.4 on 2022-12-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_alter_videomodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='file',
            field=models.FileField(null=True, upload_to='', verbose_name=''),
        ),
    ]