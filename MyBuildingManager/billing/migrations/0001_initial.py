# Generated by Django 4.2.7 on 2023-12-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.PositiveIntegerField()),
                ('electric', models.PositiveIntegerField()),
                ('gas', models.PositiveIntegerField()),
                ('charge', models.PositiveIntegerField()),
                ('others', models.PositiveIntegerField()),
                ('details', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.profile')),
            ],
        ),
    ]