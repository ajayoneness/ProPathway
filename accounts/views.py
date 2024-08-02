from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student,Domain,Assignment,AssignmentSubmit
import razorpay
from ProPathway.settings import RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET
from django.core.mail import send_mail
import random






def emailTemplate(subject,message,html_message,from_email,recipient_list):
    subject = subject
    message = message
    html_message = html_message
    from_email = from_email
    recipient_list = recipient_list

    print(subject,message,html_message,from_email,recipient_list)
    try:
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    except:
        return redirect("logout")




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

            if user.otp is None:
                request.session['otp'] = random.randint(1000, 9999)
                return redirect("otp")

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
            try: 
                Student.objects.create_user(email=email, name=name, password=password1)
           

                user = authenticate(request, email=email, password=password1)
                login(request, user)

                if user.phone_no is None:
                    request.session['otp'] = random.randint(1000, 9999)
                    return redirect("otp")

                if user.profile_pic is None:
                    return redirect('profileimage')



                print("Register Success / Login Success")

            #18Feb


            #Email

        
                return redirect('dashboard')
            except:
                messages.error(request, f'{email} is Already Registered.')

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

    if request.user.phone_no:
        return redirect('dashboard')
    else:
        return render(request, 'profileupdate.html',{'domain':domain})



@login_required(login_url='/')
def ProfileImage(request):
    
    if request.method == 'POST':
        pimage = request.FILES['profileimage']
        request.user.profile_pic = pimage
        request.user.level_student = 1
        request.user.save()

        subject = f'Thankyou For Registation'
        message = 'Thankyou For Becoming codeAj Family'
        html_message = f'''
                                            <div style="text-align:center;" >
                                                <img src ="https://www.codeajay.in/static/codeaj1.png" width=100px >
                                                <h2>codeAj</h2>
                                                <p>Internship</p>
                                            </div>
                                            <br><br>

                                            <h1 style="text-align:center;">
                                            Congratulations!
                                            </h1>
                                        
                                            <p style="text-align:center;"> You are now successfully registered as a {request.user.domain} for our Internship Program. Welcome to the CodeAj family! Thank you for joining us on this exciting journey.</p>
                                            <br><br>
                                            '''

        from_email = 'pythoncoding4u@gmail.com'
        recipient_list = ['pythoncoding4u@gmail.com',f'{request.user.email}']
        emailTemplate(subject,message,html_message,from_email,recipient_list)

        return redirect('dashboard')
    

    if request.user.profile_pic:
        return redirect('dashboard')
    else :
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

    if request.user.otp is None:
        return redirect("otp")
    
    elif request.user.phone_no is None:
        return redirect("profileupdate")

    elif request.user.profile_pic is None:
        return redirect('profileimage')
    else:
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
        if request.user.level_student !=5:  
            request.user.level_student = 2
        request.user.assignment1status = 'under_review'
        request.user.save()

        return redirect('dashboard')
    
    if request.user.assignment1status != 'under_review':
        request.user.assignment1status = 'in_progress'
        request.user.save()


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
        if request.user.level_student !=5:
            request.user.level_student = 3
        request.user.assignment2status = 'under_review'
        request.user.save()

        return redirect('dashboard')
    
    if request.user.assignment2status != 'under_review':
        request.user.assignment2status = 'in_progress'
        request.user.save()


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
        if request.user.level_student !=5:
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





@login_required(login_url='/')
def Profile(request):
    return render(request,"profile.html")








@login_required(login_url='/')
def OTP(request):

    if request.user.otp:
        return redirect('dashboard')
        
        
    else:
        try:
            print(request.session.get('otp'))
            emailTemplate("OTP | codeAj Internship","Your OTP",f"<h1 style='text-align:center; background-color:black; color:white;  padding-top:200px; padding-bottom:200px; '>{request.session.get('otp')}</h1>","codeaj4u@gmail.com",[f'{request.user.email}'])
        except:
            return redirect("login")
        
        if request.method == "POST":
            otp = request.POST['otp']
            generated_otp = request.session.get('otp')


            print(f"otp : {str(otp)}    generated otp: {str(generated_otp)}")

            if str(otp) == str(generated_otp):
                request.user.otp = 1
                request.user.save()
                print("otp_verify")
                return redirect('profileupdate')

            else:
                return render(request,"otp.html",{"message":f"Incorrect OTP !!"})
        
        
        return render(request,"otp.html",{"message":""})

            
        




















