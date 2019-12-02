from django.db import models

# Create your models here.

#class user_info(models.Model):
    #uid = models.CharField(max_length=20)
    #pwd = models.CharField(max_length=20)
    #email = models.CharField(max_length=30)



class scholarship_info(models.Model):
    objects = models.Manager()
    uid = models.CharField(max_length=50, default="")               #아이디
    school = models.CharField(max_length=50, default="")            #학교
    grade = models.CharField(max_length=50, default="")             #학점
    year = models.CharField(max_length=50, default="")              #학년
    credit = models.CharField(max_length=50, default="")            #(전학기)이수학점
    income = models.IntegerField(blank=True, null=True)             #소득분위
    impaired = models.CharField(max_length=10, default="")          #장애 여부
    merit = models.CharField(max_length=10, default="")             #국가 보훈
    major = models.CharField(max_length=50, default="")             #문과/이과/예체능 
    regular_decision = models.CharField(max_length=10, default="")  #입학 유형
