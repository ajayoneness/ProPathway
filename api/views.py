from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import Student, Domain, Assignment, AssignmentSubmit
from .serializers import StudentSerializer, DomainSerializer, AssignmentSerializer, AssignmentSubmitSerializer























class TestAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})

class LoginUserAPIView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': 'Already logged in'})

        email = request.data.get('email')
        password = request.data.get('password1')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.phone_no is None:
                return Response({'message': 'Redirect to profileupdate'})
            if user.profile_pic == "":
                return Response({'message': 'Redirect to profileimage'})
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid login credentials'}, status=status.HTTP_400_BAD_REQUEST)




class RegisterAPIView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message': 'Already registered'})

        email = request.data.get('email')
        name = request.data.get('name')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if email and name and password1 and password1 == password2:
            student = Student.objects.create_user(email=email, name=name, password=password1)

            user = authenticate(request, email=email, password=password1)
            login(request, user)

            if user.phone_no is None:
                return Response({'message': 'Redirect to profileupdate'})
            if user.profile_pic is None:
                return Response({'message': 'Redirect to profileimage'})

            return Response({'message': 'Registration successful'})
        else:
            return Response({'message': 'Invalid registration details'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdateAPIView(APIView):
    def post(self, request):
        contactno = request.data.get('contactno')
        whatsappno = request.data.get('whatsappno')
        collage = request.data.get('collage')
        domain = request.data.get('domain')

        request.user.phone_no = contactno
        request.user.whatsapp_no = whatsappno
        request.user.college = collage
        request.user.domain = Domain.objects.get(domain_name=domain)
        request.user.save()

        domn = Domain.objects.get(domain_name=domain)
        random_assignment_level1 = Assignment.objects.filter(level=1, domain=domn).order_by('?').first()
        request.user.assignment1 = random_assignment_level1
        request.user.save()

        random_assignment_level2 = Assignment.objects.filter(level=2, domain=domn).order_by('?').first()
        request.user.assignment2 = random_assignment_level2
        request.user.save()

        random_assignment_level3 = Assignment.objects.filter(level=3, domain=domn).order_by('?').first()
        request.user.assignment3 = random_assignment_level3
        request.user.save()

        return Response({'message': 'Redirect to profileimage'})

class ProfileImageAPIView(APIView):
    def post(self, request):
        pimage = request.FILES.get('profileimage')
        request.user.profile_pic = pimage
        request.user.level_student = 1
        request.user.save()
        return Response({'message': 'Profile image updated'})

class LogoutUserAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'Logged out'})

class LevelAPIView(APIView):
    def get(self, request):
        if request.user.phone_no is None:
            return Response({'message': 'Phone number missing'}, status=status.HTTP_400_BAD_REQUEST)
        if request.user.profile_pic == "":
            return Response({'message': 'Profile picture missing'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'You are at Level API view!'})

class DashboardAPIView(APIView):
    def get(self, request):
        return Response({'message': 'You are at Dashboard API view!'})

class LevelOneAPIView(APIView):
    def post(self, request):
        git = request.data.get('git')
        linkedin = request.data.get('linkedin')

        try:
            assignment_one = AssignmentSubmit.objects.get(student=request.user)
            assignment_one.Assignment1_github_Link = git
            assignment_one.Assignment1_linkedin_link = linkedin
            assignment_one.save()
        except AssignmentSubmit.DoesNotExist:
            AssignmentSubmit.objects.create(student=request.user, Assignment1_github_Link=git,
                                            Assignment1_linkedin_link=linkedin)

        request.user.level_student = 2
        request.user.save()

        return Response({'message': 'You are at Level One API view!'})

class LevelTwoAPIView(APIView):
    def post(self, request):
        git = request.data.get('git')
        linkedin = request.data.get('linkedin')

        try:
            assignment_two = AssignmentSubmit.objects.get(student=request.user)
            assignment_two.Assignment2_github_Link = git
            assignment_two.Assignment2_linkedin_link = linkedin
            assignment_two.save()
        except AssignmentSubmit.DoesNotExist:
            AssignmentSubmit.objects.create(student=request.user, Assignment2_github_Link=git,
                                            Assignment2_linkedin_link=linkedin)

        request.user.level_student = 3
        request.user.save()

        return Response({'message': 'You are at Level Two API view!'})

class LevelThreeAPIView(APIView):
    def post(self, request):
        git = request.data.get('git')
        linkedin = request.data.get('linkedin')

        try:
            assignment_three = AssignmentSubmit.objects.get(student=request.user)
            assignment_three.Assignment3_github_Link = git
            assignment_three.Assignment3_linkedin_link = linkedin
            assignment_three.save()
        except AssignmentSubmit.DoesNotExist:
            AssignmentSubmit.objects.create(student=request.user, Assignment3_github_Link=git,
                                            Assignment3_linkedin_link=linkedin)

        request.user.level_student = 4
        request.user.save()

        return Response({'message': 'You are at Level Three API view!'})

class CertificationAPIView(APIView):
    def get(self, request):
        return Response({'message': 'You are at Certification API view!'})

