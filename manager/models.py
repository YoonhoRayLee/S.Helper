from django.db import models

# Create your models here.

class Scholarship(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    credit = models.CharField(max_length=50, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    impaired = models.CharField(max_length=10, blank=True, null=True)
    merit = models.CharField(max_length=10, blank=True, null=True)
    major = models.CharField(max_length=50, blank=True, null=True)
    regular_decision = models.CharField(max_length=10, blank=True, null=True)
    period = models.CharField(max_length=50, blank=True, null=True)
    benefit = models.CharField(max_length=50, blank=True, null=True)
    spec = models.CharField(max_length=60, blank=True, null=True)
    stype = models.CharField(max_length=50, blank=True, null=True)

class User_Contest(models.Model):
    objects = models.Manager()
    user_id = models.CharField(max_length=50, default="")
    contest_id = models.CharField(max_length=50, default="")

class User_Scholarship(models.Model):
    objects = models.Manager()
    user_id = models.CharField(max_length=50, default="")
    scholarship_id = models.CharField(max_length=50, default="")

class Contest(models.Model):
    objects = models.Manager()
    company = models.CharField(max_length=50, blank=True, null=True)
    Ctype = models.CharField(max_length=50, blank=True, null=False)
    title = models.CharField(max_length=50, blank=True, null=False)
    content = models.CharField(max_length=500, blank=True, null=True)
    sdate = models.DateField(auto_now=False)
    edate = models.DateField(auto_now=False)

class Notice(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=500, default="", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.post_title
    
    def update_counter(self):
        self.hit = self.hit + 1
        self.save()

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    exchange_id = models.CharField(max_length=255,null=True,blank=True)
    event_start = models.DateTimeField(null=True,blank=True)
    event_end = models.DateTimeField(null=True,blank=True)
    event_subject = models.CharField(max_length=255,null=True,blank=True)
    event_location = models.CharField(max_length=255,null=True,blank=True)
    event_category = models.CharField(max_length=255,null=True,blank=True)
    event_attendees = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.event_subject
