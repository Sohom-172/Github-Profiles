from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(AbstractUser):
	#user = models.OneToOneField(User,on_delete=models.CASCADE)
	#email = models.EmailField(max_length=256,default='')
	github_full_name = models.CharField(max_length = 100,default='')
	#first_name = models.CharField(max_length = 100,default='')
	#last_name = models.CharField(max_length = 100,default='')
	github_link = models.URLField(default='')
	github_followers = models.IntegerField(default=0)
	github_repos = models.URLField(default='')
	updated_at = models.CharField(max_length = 100,default='')

'''
class Repository(models.Model):
	owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
	repo_name = models.CharField(max_length=100,default='')
	star_count = models.IntegerField()
'''

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)