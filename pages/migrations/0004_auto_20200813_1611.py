# Generated by Django 3.0.8 on 2020-08-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200813_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecategory',
            name='category_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]