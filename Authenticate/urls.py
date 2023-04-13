# from django.conf.urls import url 
from django.urls import include, path,re_path
from Authenticate import views 
# from corsheaders.views import cors_exempt

from .views import LoginView

urlpatterns = [ 
             
    path('user_api/', views.user_list),
    path('user_api/<int:pk>', views.user),
    # path('user_api/uses/', views.user_list_published),
    
    
    path('login/',LoginView.as_view(),name='login'),
    
    # path('login/',views.user),
    
    
    path('role_list_api/', views.role_list),
    path('role_list_api/<int:pk>', views.role_detail),
    # path('role_api/roles/', views.role_list_published),
    
    path('user_details_list_api/', views.user_details_list),
    path('user_details_list_api/<int:pk>', views.user_detail),
    
    path('module_list_api/', views.module_list),
    path('module_list_api/<int:pk>', views.module_detail),


]
