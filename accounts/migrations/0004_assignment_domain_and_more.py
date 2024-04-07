# Generated by Django 5.0 on 2024-01-27 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_student_date_joined_student_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.domain'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assignment_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assignment_requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='level',
            field=models.IntegerField(choices=[(0, 'Not Started'), (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Certificate Level')], default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='referral_link1',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='referral_link2',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level_student',
            field=models.IntegerField(choices=[(0, 'Not Started'), (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Certificate Level')], default=0),
        ),
    ]
