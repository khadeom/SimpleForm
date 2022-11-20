from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings


PHONENO_REGEX='^[0-9]{10}$'
from django.utils import timezone

class incidentData(models.Model):
    location = models.CharField(max_length=100,default="")

    incident_department = models.CharField(max_length=100,default="")

    date_time = models.DateTimeField(default=timezone.now)

    incident_location = models.CharField(max_length=50,default="")
    initial_severity = models.CharField(max_length=50,default="")
    immidiate_action_taken = models.CharField(max_length=100,default="")

    enviornmentalincident = models.BooleanField(default=False)
    injury_illness = models.BooleanField(default=False)
    property_damage = models.BooleanField(default=False)
    vehicle = models.BooleanField(default=False)

    reported_by = models.CharField(max_length=50,default="")




    # user                        =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # name                        =   models.CharField(max_length=200)
    # ha                        =   models.CharField(max_length=200)

    # phone_number                =   models.CharField(max_length=200,validators=[RegexValidator(
    #                                         regex=PHONENO_REGEX,
    #                                         message="Phone Number must be of 10 digits",
    #                                         code='invalid_username'
    #                                         )])
    # email_address               =   models.EmailField(null=True, blank=True)
    # spam_count                  =   models.IntegerField(default=0)
    # def __str__(self):
    #     return self.name