from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
   path('',views.index, name='index'),
   path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
   path('update-profile',views.update_profile, name='update_profile'),
   path('profile/<pk>',views.profile, name = 'profile'),
   path('search/',views.search_results, name='search_results'),
   path('submit-project',views.submit_project, name='submit_project'),
   path('site_details/<int:id>/',views.site_details,name='site_details'),
   path('rate/<int:id>/',views.rate_project,name='rate_project'),
   path('api/projects/', views.ProjectList.as_view()),
   path('api/profiles/', views.ProfileList.as_view()),
]
