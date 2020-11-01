# Generated by Django 3.0.8 on 2020-08-13 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200723_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='page_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.PageCategory'),
        ),
    ]
