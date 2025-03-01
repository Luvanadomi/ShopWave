# Generated by Django 5.0.6 on 2024-07-05 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inbox',
            options={'ordering': ('-modified_at',)},
        ),
        migrations.CreateModel(
            name='InboxMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('conservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='inbox.inbox')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
