from django.db import models



class Mentor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='mentors/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    expertise = models.CharField(max_length=255) 
    experience = models.PositiveIntegerField()  
    linkedin_profile = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    one_hour_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    one_Project_guide_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    all_3_Project_guide_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
