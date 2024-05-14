# Generated by Django 5.0.3 on 2024-03-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
