from django.shortcuts import render
from .models import Mentor
from django.http import JsonResponse



def mentor(request):
    # mentor = Mentor.objects.all()
    # return render(request, 'mentor.html',{'mentor':mentor})
    return render(request, 'mentor.html')



def mentor_list(request):
    mentors = Mentor.objects.all()
    mentor_data = []
    
    for mentor in mentors:
        mentor_data.append({
            'name': mentor.name,
            'email': mentor.email,
            'phone_number': mentor.phone_number,
            'whatsapp_number': mentor.whatsapp_number,
            'profile_picture': mentor.profile_picture.url if mentor.profile_picture else None,
            'bio': mentor.bio,
            'expertise': mentor.expertise,
            'experience': mentor.experience,
            'linkedin_profile': mentor.linkedin_profile,
            'website': mentor.website,
            'one_hour_price': str(mentor.one_hour_price) if mentor.one_hour_price else None,
            'one_Project_guide_price': str(mentor.one_Project_guide_price) if mentor.one_Project_guide_price else None,
            'all_3_Project_guide_price': str(mentor.all_3_Project_guide_price) if mentor.all_3_Project_guide_price else None,
            'created_at': mentor.created_at,
            'updated_at': mentor.updated_at,
        })

    return JsonResponse(mentor_data, safe=False)