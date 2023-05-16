# Generated by Django 4.1.5 on 2023-05-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='ruffiertest',
            name='user',
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='RuffierTest',
        ),
    ]
