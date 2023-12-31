# Generated by Django 4.2.7 on 2023-11-16 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myauth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('status', models.CharField(choices=[('Pending', 'Pend'), ('Replied', 'Rep')], default='Pending', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TicketReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('parent_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.ticket')),
            ],
        ),
    ]
