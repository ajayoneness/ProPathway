# Generated by Django 4.0 on 2024-08-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_student_assignment1endttime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='assignment1rejectioncount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignment2rejectioncount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignment3rejectioncount',
            field=models.IntegerField(default=0),
        ),
    ]