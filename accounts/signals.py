from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student

@receiver(post_save, sender=Student)
def send_update_email(sender, instance, created, **kwargs):
    if not created:  # The instance was updated, not created

        if instance.level_student == 5:
            try:
                send_mail(
            'Status Updated',

            f'''
Now You are Successfully Verified !! Now you can get your certificate !! 

Current Level : {instance.level_student}
Assignment 1 staus : {instance.assignment1status}
Assignment 2 staus : {instance.assignment2status}
Assignment 3 staus : {instance.assignment3status}

Note : After your all the 3 Assignment Will be completed then only you can get the Certificate
''',

            'ajayoneness123@gmail.com',  
            ['codeaj4u@gmail.com',f'{instance.email}'], 
            fail_silently=False,
        )
            except:
                print("mail not sent")

        # else:
        #     try:
        #         send_mail(
        #         'Status Updated',

        #         f'''

        #                 Your all level are not completed kindly complete all three level than only you can move to the certification level
        #                 Current Level : {instance.level_student}
        #                 Assignment 1 staus : {instance.assignment1status}
        #                 Assignment 2 staus : {instance.assignment2status}
        #                 Assignment 3 staus : {instance.assignment3status}

        #                 Note : After your all the 3 Assignment Will be completed then only you can get the Certificate
        #                 ''',

        #         'ajayoneness123@gmail.com',  
        #         ['codeaj4u@gmail.com',f'{instance.email}'], 
        #         fail_silently=False,
        #         )
        #         print("mail sent complete")
            
        #     except:
        #         print("mail not sent")
