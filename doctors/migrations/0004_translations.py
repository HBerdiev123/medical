# Generated by Django 3.0.8 on 2020-08-16 18:55

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20200725_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialization',
        ),
        migrations.CreateModel(
            name='DoctorTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('specialization', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=70, null=True)),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contact_info', ckeditor.fields.RichTextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='doctors.Doctor')),
            ],
            options={
                'verbose_name': 'doctor Translation',
                'db_table': 'doctors_doctor_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
