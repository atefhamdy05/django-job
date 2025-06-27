from django.urls import path,include
from . import views
app_name='jobs'
urlpatterns = [
   
    path('signup',views.signup,name='signup'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    
     
]