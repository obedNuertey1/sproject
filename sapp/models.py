from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class SModel(models.Model):
    #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #emailAdd = models.CharField(max_length=100)
    #password = models.CharField(('password'), max_length=128)
    #password2 = models.CharField(('confirm-password'), max_length=128)
    isComplete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    #student_ID = models.CharField(max_length=20)
    #PIN = models.CharField(('PIN'), max_length=12)
    pdf_file = models.FileField(upload_to='Users/user/Desktop/sproject/media')

    def __str__(self):
        return "%s's profile" % self.first_name


# def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        profile, created = SModel.objects.get_or_create(user=instance)


#post_save.connect(create_user_profile, sender=User)
