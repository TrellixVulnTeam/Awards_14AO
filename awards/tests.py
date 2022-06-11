from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile, Review

# Create your tests here.
class ProfileTestCases(TestCase):
    def setUp(self):
        self.new_profile = Profile(id=1, user='Chacha', profile_picture='example.jpg', bio='Live life',
                                   email='chacha@gmail.com', phone_number='0725470100',username='chacha')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        all_obj = Profile.objects.all()
        self.assertTrue(len(all_obj) > 0)
        
class ProjectTestCases(TestCase):
    def setUp(self):
        self.new_project = Project(id=1,user='Chacha',title='Instagram', image='exampl.jpg',description='Description',link='www.instagram.com',country='Kenya')
        self.new_project.save_project()

    def tearDown(self):
        Project.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_method(self):
        self.new_project.save_project()
        all_obj = Project.objects.all()
        self.assertTrue(len(all_obj)>0)  
        
class ReviewTestCases(TestCase):
    def setUp(self):      
        self.new_review = Review(id=1,user='Chacha',project='Instagram',design='1',usability='1',content='1',overall='1',comment='comment')
        self.new_review.save_review()
        
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
                