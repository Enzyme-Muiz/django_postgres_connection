from django.db import models

# Create your models here.
class room_descriptions(models.Model):
    room_description= models.CharField(max_length = 40)
    def __str__(self):
        return self.room_description
    
class JacksonDrivePeople(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 50)
    Date_of_birth = models.DateField()
    room_number_value = models.ForeignKey(room_descriptions, default = None, on_delete=models.DO_NOTHING)
    def __str__(self):
        return (self.first_name + " " + self.last_name)
    


