# Generated by Django 4.2.4 on 2023-08-13 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RotateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.IntegerField()),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='upload.imagemodel')),
            ],
        ),
    ]
