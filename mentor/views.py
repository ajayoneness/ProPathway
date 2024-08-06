from django.shortcuts import render
from .models import Mentor



def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html',{'mentor':mentor})
