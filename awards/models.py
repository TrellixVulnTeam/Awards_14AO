from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models import Q


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    username = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.user 

    
class Project(models.Model):   
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='project_user')
    title = models.CharField(max_length=100)
    image = CloudinaryField('image') 
    description = HTMLField()
    link = models.CharField(max_length=250)
    posted_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, default="")
  
    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(Q(user__username=search_term) | Q(title__icontains=search_term))
        return projects  
      
    
    def __str__(self):
        return self.title        
    
RATE_CHOICES = [
	(1,'1 - Unsatisfactory'),
	(2,'2 - Pathetic'),
	(3,'3 - Very bad'),
	(4,'4 - Bad'),
	(5,'5 - Average'),
	(6,'6 - Okay'),
	(7,'7 - Good'),
	(8,'8 - Very Good'),
	(9,'9 - Excellent'),
	(10, '10 - Perfect'), 
]



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    design = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5) 
    usability =models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5)  
    content = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=5)
    comment = models.CharField(max_length=250, blank=True,default='')  
    overall = models.IntegerField(blank=True,default=0)   
