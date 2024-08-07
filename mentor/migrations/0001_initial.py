# Generated by Django 4.0 on 2024-08-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='mentors/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('expertise', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField()),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('one_hour_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('one_Project_guide_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('all_3_Project_guide_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
