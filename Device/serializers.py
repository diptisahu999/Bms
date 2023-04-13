from rest_framework import serializers 

from Device.models import Bms_bulding_master,Bms_floor_master,Bms_department_master,Bms_sub_area_master,Bms_locker,Bms_device_master,Bms_hardware_type,Bms_device_type,Bms_device_status_history,Bms_user_area_cards_list

class Bms_Bulding_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_bulding_master
        fields=['id','tower_name']
        
        
class Bms_floor_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_floor_master
        fields=['id','floor_name',]
        
        
class Bms_department_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_department_master
        fields=['id','department_name',]
        
        
class Bms_sub_area_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_sub_area_master
        fields=['id','sub_area_name','width','height','on_image_path','off_image_path']
        
        
class Bms_locker_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_locker
        fields=['id','locker_name','category','status','created_at','updated_at']



class Bms_Devices_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_device_master

        fields='__all__'



class Bms_hardware_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_hardware_type

        fields='__all__'



class Bms_device_status_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_device_status_history

        fields='__all__'

    
class Bms_device_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_device_type

        fields='__all__'
        

class Bms_user_area_cards_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_user_area_cards_list

        fields='__all__'