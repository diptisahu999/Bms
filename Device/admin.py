from django.contrib import admin
from .models import Bms_bulding_master, Bms_floor_master, Bms_department_master, Bms_sub_area_master, Bms_locker, Bms_access_control_rfid_master, Bms_history, Bms_settings, Bms_device_master, Bms_hardware_type, Bms_device_type, Bms_device_status_history, Bms_user_area_cards_list

# Register your models here.


@admin.register(Bms_bulding_master)
class Bms_building_masterAdmin(admin.ModelAdmin):
    list_display = ['id', 'tower_name', 'created_at', 'updated_at']


@admin.register(Bms_floor_master)
class Bms_floor_masterAdmin(admin.ModelAdmin):
    list_display = ['id', 'floor_name', 'created_at', 'updated_at']


@admin.register(Bms_department_master)
class Bms_department_masterAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name', 'created_at', 'updated_at']


@admin.register(Bms_sub_area_master)
class Bms_sub_area_masterAdmin(admin.ModelAdmin):
    list_display = ['id', 'sub_area_name', 'on_image_path', 'off_image_path',
                    'width', 'height', 'seating_capacity', 'created_at', 'updated_at']


@admin.register(Bms_locker)
class Bms_lockerAdmin(admin.ModelAdmin):
    list_display = ['id', 'locker_name', 'category',
                    'status', 'created_at', 'updated_at']


@admin.register(Bms_access_control_rfid_master)
class Bms_access_control_rfid_masterAdmin(admin.ModelAdmin):
    list_display = ['id', 'rfid_no', 'card_type', 'status',
                    'access_start_time', 'access_end_time', 'created_at', 'updated_at']


@admin.register(Bms_history)
class Bms_historyAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'description', 'created_at']


@admin.register(Bms_settings)
class Bms_settingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'setting_data', 'created_at']


@admin.register(Bms_device_master)
class Bms_deviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'STATUS', 'device_name', 'created_at', 'device_informations',
                    'status', 'is_user', 'create_at', 'updated_user_details_date']


@admin.register(Bms_hardware_type)
class Bms_hardware_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']


@admin.register(Bms_device_type)
class Bms_device_type_admin(admin.ModelAdmin):
    list_display = ['id',
        'name',
        'created_at',
    ]


@admin.register(Bms_device_status_history)
class Bms_device_status_history_admin(admin.ModelAdmin):
    list_display = ['id',
                    'status']


@admin.register(Bms_user_area_cards_list)
class Bms_user_area_cards_list_admin(admin.ModelAdmin):
    list_display = ['id',
        'card_id',
        'card_name',
        'created_at',
        'status']
