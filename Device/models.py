from django.db import models
from django.utils import timezone
# from Authodication.models import Bms_Users,Bms_Module_master



# Create your models here
class Bms_bulding_master(models.Model):
    tower_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tower_name
    
class Bms_floor_master(models.Model):
    tower_id=models.ManyToManyField(Bms_bulding_master,blank=True)
    floor_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.floor_name
    
    
class Bms_department_master(models.Model):
    department_name=models.CharField(max_length=100)
    floor_id=models.ManyToManyField(Bms_floor_master,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.department_name
    
    
class Bms_sub_area_master(models.Model):
    sub_area_name=models.CharField(max_length=100)
    department_id=models.ManyToManyField(Bms_department_master, blank=True)
    on_image_path = models.CharField(max_length=255)
    off_image_path = models.CharField(max_length=255)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    seating_capacity=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sub_area_name
    
    
class Bms_locker(models.Model):
    CATEGORIES=[
        ("N","Normal"),
        ("B","Big"),
    ]
    
    STATUS= [
    ("A","Active"),
    ("N","Inactive"),
    ]
    
    locker_name=models.CharField(max_length=100)
    sub_area_id=models.ManyToManyField(Bms_sub_area_master, blank=True)
    category=models.CharField(max_length=100,choices=CATEGORIES)
    status=models.CharField(max_length=100, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.locker_name
    
class Bms_access_control_rfid_master(models.Model):
    CARD_TYPES=[
        ('N','No-assign'),
        ('S','Static'),
        ('D','Dynamic')
    ]
    
    STATUS= [
    ("A","Active"),
    ("N","Inactive"),
    ]
    
    rfid_no=models.IntegerField()
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users')
    # user_id=models.ManyToManyField(Bms_Users,blank=True)
    card_type=models.CharField(max_length=100, choices=CARD_TYPES)
    access_area_id=models.ManyToManyField(Bms_sub_area_master,blank=True)
    status=models.CharField(max_length=100, choices=STATUS)
    access_start_time=models.DateField(default=timezone.now)
    access_end_time=models.DateField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.rfid_no)
    

class Bms_history(models.Model):
    TYPES=[
        ('N','Newuser'),
        ('V','Visitor'),
        ('A','Access'),
        ('C','Conference'),
    ]
    
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users', blank=True)
    # user_id=models.ManyToManyField(Bms_Users, blank=True)
    type=models.CharField(max_length=100, choices=TYPES)
    description=models.JSONField(default=dict, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.type
    

class Bms_settings(models.Model):
    module_id=models.ManyToManyField(to='Authenticate.Bms_Module_master',blank=True)
    # module_id=models.ManyToManyField(Bms_Module_master,blank=True)
    setting_data=models.JSONField(default=dict, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
class Bms_hardware_type(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=12,blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table='bms_hardware_tbl'
        
        
class Bms_device_type(models.Model):
    hardware_type_id=models.ManyToManyField(Bms_hardware_type)
    name=models.CharField(max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table='bms_device_tbl'
        
        
class Bms_device_master(models.Model):
    STATUS= [
        ("Yes","Yes"),
        ("No","No"),
        
    ]
    # hardware_type_id=models.ManyToManyField(Bms_hardware_type,related_name='device')
    device_type=models.ManyToManyField(Bms_device_type)
    device_name=models.CharField(max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    device_informations=models.TextField(max_length=2244)
    status = models.BooleanField(default=False)
    is_user=models.CharField(max_length=23,choices=STATUS)
    create_at=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name
    
    class Meta():
        db_table='bms_device_master_tbl'
        
        
class Bms_device_status_history(models.Model):
    device_id=models.ManyToManyField(Bms_sub_area_master,related_name='device_id')
    status = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.device_name
    
    class Meta():
        db_table='bms_device_status_tbl'


class Bms_user_area_cards_list(models.Model):
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users', blank=True)
    card_id=models.IntegerField()
    card_name=models.JSONField()
    created_at=models.DateTimeField(default=timezone.now)
    department_id=models.ManyToManyField(Bms_department_master)
    # floor_id=models.ManyToManyRel(Bms_floor_master)
    status = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.device_name
    
    class Meta():
        db_table='bms_user_area_cards_list_tbl'
    