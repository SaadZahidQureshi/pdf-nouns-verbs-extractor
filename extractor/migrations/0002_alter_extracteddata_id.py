# Generated by Django 4.1.13 on 2024-05-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracteddata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
