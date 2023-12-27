from django.db import migrations, models
import django.db.models.deletion

# Migration for Ticketing app models: Ticket and TicketReply

class Migration(migrations.Migration):
    # This is the initial migration for the Ticketing app

    initial = True

    dependencies = [
        ('myauth', '__first__'),
    ]

    operations = [
        # Model for tickets
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('status', models.CharField(
                    max_length=10,
                    choices=[('Pending', 'Pending'), ('Replied', 'Replied')],
                    default='Pending',
                    verbose_name='Status'
                )),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.profile', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        # Model for ticket replies
        migrations.CreateModel(
            name='TicketReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('parent_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.ticket', verbose_name='Parent Ticket')),
            ],
            options={
                'verbose_name': 'Ticket Reply',
                'verbose_name_plural': 'Ticket Replies',
            },
        ),
    ]
