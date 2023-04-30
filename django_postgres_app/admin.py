from django.contrib import admin

# Register your models here.

from .models import room_descriptions, JacksonDrivePeople

all_models = [room_descriptions, JacksonDrivePeople]
admin.site.register(all_models)
