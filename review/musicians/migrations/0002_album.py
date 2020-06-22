# Generated by Django 3.0.7 on 2020-06-22 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.Musician')),
            ],
        ),
    ]
