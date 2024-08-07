from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Discussions, discussionReply
from accounts.models import Student
from accounts.models import Assignment
import json
from django.http import HttpResponse




def Discussion(request, slug):
    ass = get_object_or_404(Assignment, slug=slug)
    stu = get_object_or_404(Student, id=request.user.id)
    

    if request.method == "POST":
        if 'commentNow' in request.POST:
            comment = request.POST.get('comment')
            if comment:
                Discussions.objects.create(assignment=ass, student=stu, comment=comment)


        if 'comment_replay' in request.POST:
            comment_reply = request.POST.get('commentreply')
            comment_id = request.POST.get('comment_id')
            disc = get_object_or_404(Discussions, id=comment_id)

            if comment_reply:
                discussionReply.objects.create(discuss=disc, student=stu, comment=comment_reply)

            print(comment_reply,comment_id)





    discussion  = Discussions.objects.filter(assignment=ass).order_by("-id")
    discussionreply  = discussionReply.objects.all().order_by("-id")


    return render(request, 'discussion.html', {'assignment': ass, 'discuss' : discussion, "disrep":discussionreply })

