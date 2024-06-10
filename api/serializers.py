from rest_framework import serializers
from accounts.models import Student, Domain, Assignment, AssignmentSubmit

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'domain_name', 'domain_description']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'domain', 'assignment_question', 'assignment_description', 'assignment_requirements',
                  'assignment_banner', 'assignment_banner1', 'level', 'referral_link1', 'referral_link2']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'email', 'name', 'profile_pic', 'phone_no', 'whatsapp_no', 'college', 'domain',
                  'assignment1', 'assignment2', 'assignment3', 'level_student', 'is_active', 'is_staff',
                  'date_joined']

class AssignmentSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmit
        fields = ['id', 'student', 'Assignment1_github_Link', 'Assignment1_linkedin_link',
                  'Assignment2_github_Link', 'Assignment2_linkedin_link',
                  'Assignment3_github_Link', 'Assignment3_linkedin_link']
        


