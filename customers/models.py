from django.db import models

# Create your models here.
class customersDetailsModel(models.Model):
    age = models.IntegerField()
    balance = models.BigIntegerField(default=None)
    campaign = models.IntegerField(default=None)
    contact = models.CharField(max_length=35,default=None)
    #job = [('admin','admin'),('blue-collar','blue-collar'),('entrepreneur','entrepreneur'),('housemaid','housemaid'),('management','management'),('retired','retired'),('self-employed','self-employed'),('services','services'),('student','student'),('technician','technician'),('unemployed','unemployed'),('unknown','unknown')]
    job = models.CharField(max_length=35)
    day = models.IntegerField(default=None)
    #Default = models.CharField(max_length=10)
    duration = models.IntegerField(default=None)
    #housing = [('yes','yes'),('no','no')]
    housing = models.CharField(max_length=35)
    #loan = [('yes','yes'),('no','no')]
    loan = models.CharField(max_length=35)
    #Marital = [('Married','Married'),('Single','Single'),('Divorced','Divorced')]
    marital = models.CharField(max_length=35)
    #Education = [('primary','primary'),('secondary','secondary'),('tertiary','tertiary'),('unknown','unknown')]
    education = models.CharField(max_length=35)
    #month = [('Jan','Jan'),('Feb','Feb'),('Mar','Mar'),('Apr','Apr'),('May',"May"),('Jun','Jun'),('July','July'),('Aug','Aug'),('Sept','Sept'),('Oct','Oct'),('Nov','Nov'),('Dec','Dec')]
    month = models.CharField(max_length=35)
    pdays = models.IntegerField(default=None)
    #poutcome = [('Success','Success'),('Failure','Failure'),('Other','Other'),('Unknown','Unknown')]
    poutcome = models.CharField(max_length=35)
    previous = models.IntegerField(default=None)







