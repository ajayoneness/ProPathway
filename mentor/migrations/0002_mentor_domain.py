# Generated by Django 5.0 on 2024-08-09 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_domain_mentor'),
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.domain'),
        ),
    ]
