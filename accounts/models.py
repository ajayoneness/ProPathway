from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class Domain(models.Model):
    domain_name = models.CharField(max_length=255)
    domain_description = models.TextField()
   


    def __str__(self):
        return self.domain_name
    

class RefralLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title



class Assignment(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True, blank=True)
    assignment_question = models.CharField(max_length=255)
    assignment_description = models.TextField(null=True, blank=True)
    assignment_requirements = models.TextField(null=True, blank=True)
    assignment_banner = models.ImageField(upload_to='assignment_banners/', null=True, blank=True)
    assignment_banner1 = models.ImageField(upload_to='assignment_banners1/', null=True, blank=True)
    level_choices = [(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')]
    level = models.IntegerField(choices=level_choices, default=0)
    links = models.ManyToManyField(RefralLink, null=True, blank=True)
    youtube_video_id = models.CharField(max_length=255,null=True, blank=True)
    # referral_link1 = models.URLField(max_length=255, null=True, blank=True)
    # referral_link2 = models.URLField(max_length=255, null=True, blank=True)

    slug = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.assignment_question} Level : {self.level}"


class StudentManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        student = self.model(email=email, name=name, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, password, **extra_fields)
    

class Student(AbstractBaseUser, PermissionsMixin):

    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_UNDER_REVIEW = 'under_review'
    STATUS_COMPLETED = 'completed'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_NOT_STARTED, 'Not Started'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_UNDER_REVIEW, 'Under Review'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_REJECTED, 'Rejected'),
    ]



    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)
    whatsapp_no = models.CharField(max_length=15, null=True, blank=True)
    college = models.CharField(max_length=255, null=True, blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True, blank=True)
    
    # assignment 1
    assignment1 = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignment1')
    assignment1status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_STARTED,
    )
    assignment1starttime = models.DateTimeField(blank=True,null=True)
    assignment1endttime = models.DateTimeField(blank=True,null=True)
    assignment1rejectioncount = models.IntegerField(default=0)

    #assignment 2
    assignment2 = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignment2')
    assignment2status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_STARTED,
    )
    assignment2starttime = models.DateTimeField(blank=True,null=True)
    assignment2endttime = models.DateTimeField(blank=True,null=True)
    assignment2rejectioncount = models.IntegerField(default=0)


    #assignment 3
    assignment3 = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignment3')
    assignment3status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_STARTED,
    )
    assignment3starttime = models.DateTimeField(blank=True,null=True)
    assignment3endttime = models.DateTimeField(blank=True,null=True)
    assignment3rejectioncount = models.IntegerField(default=0)



    level_choices_student = [(0, 'Not Started'), (1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'pending'), (5, 'Certificate Level')]
    level_student = models.IntegerField(choices=level_choices_student, default=0)
    otp = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    objects = StudentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def update_profile(self, name=None, profile_pic=None, phone_no=None, whatsapp_no=None, college=None, domain=None):
        if name:
            self.name = name
        if profile_pic:
            self.profile_pic = profile_pic
        if phone_no:
            self.phone_no = phone_no
        if whatsapp_no:
            self.whatsapp_no = whatsapp_no
        if college:
            self.college = college
        if domain:
            self.domain = domain
        self.save()


class AssignmentSubmit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    Assignment1_github_Link = models.TextField(null=True, blank=True)
    Assignment1_linkedin_link = models.TextField(null=True, blank=True)
    Assignment2_github_Link = models.TextField(null=True, blank=True)
    Assignment2_linkedin_link = models.TextField(null=True, blank=True)
    Assignment3_github_Link = models.TextField(null=True, blank=True)
    Assignment3_linkedin_link = models.TextField(null=True, blank=True)






    


