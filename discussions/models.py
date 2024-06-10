from django.db import models
from accounts.models import Assignment,Student



class Discussions(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

class discussionReply(models.Model):
    discuss = models.ForeignKey(Discussions, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)