# Generated by Django 5.0.4 on 2024-06-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_student_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
