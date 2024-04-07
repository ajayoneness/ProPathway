from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student,Domain,Assignment,AssignmentSubmit
import razorpay
from ProPathway.settings import RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET




def test(request):
    return render(request,'index.html')



def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print("login Success")
            print(user.profile_pic)
            if user.phone_no is None:
                return redirect("profileupdate")

            if user.profile_pic == "":
                return redirect('profileimage')

            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            print("inavlid")
    return render(request, 'login.html')


def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if email and name and password1 and password1 == password2:
            student = Student.objects.create_user(email=email, name=name, password=password1)

            user = authenticate(request, email=email, password=password1)
            login(request, user)

            if user.phone_no is None:
                return redirect("profileupdate")

            if user.profile_pic is None:
                return redirect('profileimage')



            print("Register Success / Login Success")

            #18Feb




            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid registration details')
    return render(request, 'register.html')





@login_required(login_url='/')
def ProfileUpdate(request):

    if request.method == "POST":
        contactno = request.POST['contactno']
        whatsappno = request.POST['whatsappno']
        collage = request.POST['collage']
        domain = request.POST['domain']

        request.user.phone_no = contactno
        request.user.whatsapp_no = whatsappno
        request.user.college = collage
        request.user.domain = Domain.objects.get(domain_name=domain)
        request.user.save()

        domn = Domain.objects.get(domain_name=domain)
        # Update assignment1 with a random assignment of level 1
        random_assignment_level1 = Assignment.objects.filter(level=1,domain=domn).order_by('?').first()
        request.user.assignment1 = random_assignment_level1
        request.user.save()

        # Update assignment2 with a random assignment of level 2
        random_assignment_level2 = Assignment.objects.filter(level=2,domain=domn).order_by('?').first()
        request.user.assignment2 = random_assignment_level2
        request.user.save()

        # Update assignment3 with a random assignment of level 3
        random_assignment_level3 = Assignment.objects.filter(level=3,domain=domn).order_by('?').first()
        request.user.assignment3 = random_assignment_level3
        request.user.save()

        return redirect('profileimage')
        #return to the profile image page



    domain = Domain.objects.all()
    return render(request, 'profileupdate.html',{'domain':domain})



@login_required(login_url='/')
def ProfileImage(request):

    if request.method == 'POST':
        pimage = request.FILES['profileimage']
        request.user.profile_pic = pimage
        request.user.level_student = 1
        request.user.save()
        return redirect('dashboard')

    return render(request, 'profileimage.html')






@login_required(login_url='/')
def logoutuser(request):
    logout(request)
    return redirect('main')






@login_required(login_url='/')
def level(request):
    if request.user.phone_no is None:
        return redirect("profileupdate")

    if request.user.profile_pic == "":
        return redirect('profileimage')

    return render(request, 'level1.html')





@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required(login_url='/')
def level_one(request):
    student = request.user
    if request.method == "POST":
        git = request.POST['git']
        linkedin = request.POST['linkedin']

        try:
            assignmet_one = AssignmentSubmit(student=student,Assignment1_github_Link=git,Assignment1_linkedin_link=linkedin)
            assignmet_one.save()
        except:
            update_assignemt_one = AssignmentSubmit.objects.get(student=student)
            update_assignemt_one.Assignment1_github_Link = git
            update_assignemt_one.Assignment1_linkedin_link = linkedin
            update_assignemt_one.save()

        request.user.level_student = 2
        request.user.save()

        return redirect('level2')
    try:
        submitted_data = AssignmentSubmit.objects.get(student=student)
        return render(request, 'level1.html',{"sdata": submitted_data})
    except:
        return render(request, 'level1.html')




@login_required(login_url='/')
def level_two(request):
    student = request.user
    if request.method == "POST":
        git = request.POST['git']
        linkedin = request.POST['linkedin']


        update_assignemt_two = AssignmentSubmit.objects.get(student=student)
        update_assignemt_two.Assignment2_github_Link = git
        update_assignemt_two.Assignment2_linkedin_link = linkedin
        update_assignemt_two.save()

        request.user.level_student = 3
        request.user.save()

        return redirect('level3')

    try:
        submitted_data = AssignmentSubmit.objects.get(student=student)
        return render(request, 'level2.html', {"sdata": submitted_data})
    except:
        return render(request, 'level2.html')



@login_required(login_url='/')
def level_three(request):
    student = request.user
    if request.method == "POST":
        git = request.POST['git']
        linkedin = request.POST['linkedin']


        update_assignemt_three = AssignmentSubmit.objects.get(student=student)
        update_assignemt_three.Assignment3_github_Link = git
        update_assignemt_three.Assignment3_linkedin_link = linkedin
        update_assignemt_three.save()

        request.user.level_student = 4
        request.user.save()

        return redirect('dashboard')

    try:
        submitted_data = AssignmentSubmit.objects.get(student=student)
        return render(request, 'level3.html', {"sdata": submitted_data})
    except:
        return render(request, 'level3.html')





@login_required(login_url='/')
def certification(request):
    return render(request, 'certificate.html')



@login_required(login_url='/')
def Pay(request):
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
    data = {"amount": 99000, "currency": "INR", "receipt": "PythonCoding4u"}
    payment = client.order.create(data=data)
    print(payment)

    return render(request, 'certificate.html', payment)




















