from django.urls import include, path,re_path
from Device import views 
from Device.device_status import getDeviceStatus
 
urlpatterns = [ 
      
             
    path('bms_Bulding_master/', views.user_list),
    path('bms_Bulding_master/<int:pk>', views.user),
    
    path('bms_floor_api/', views.floor_list),
    path('bms_floor_details_api/<int:pk>', views.floor_details),
    
    path('department_api/', views.department_list),
    path('department_details_api/<int:pk>', views.department),
    
    path('Bms_sub_area_list_api/', views.Bms_sub_area_list),
    path('Bms_sub_area_details_api/<int:pk>', views.Bms_sub_area),
    
    
    path('Bms_locker_list_api/', views.Bms_locker_list),
    path('Bms_locker_details_api/<int:pk>', views.Bms_locker_list_details),

    path('BMS_Device_List/', views.Device_list),
    # path('BMS_Devices_List/<int:pk>', views.de),
]

getDeviceStatus()