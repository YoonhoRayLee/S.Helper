from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Scholarship
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.contrib import auth


# Create your views here.
#scholarship_list = ListView.as_view(model=Scholarship)
#scholarship_detail = DetailView.as_view(model=Scholarship)

@user_passes_test(lambda u: u.is_superuser)
def show_list(request):
    if user_passes_test:
        Scholarship_list = Scholarship.objects.all()
        paginator = Paginator(Scholarship_list, 10)
        page = request.GET.get('page')
        try:
            scholarships = paginator.page(page)
        except PageNotAnInteger:
            scholarships = paginator.page(1)
        except EmptyPage:
            scholarships = paginator.page(paginator.num_pages)
        if request.method=="POST":
            sid = request.POST["sid"]

            delete_scholarship = Scholarship.objects.get(id=sid)
            delete_scholarship.delete()
            messages.info(request, '해당 장학을 삭제 했습니다!')
            return redirect("/manage/")
        return redirect("/manage/")
    else:
        return render(request, 'manage.html', {'scholarships':scholarships})

def delete_db(request):
    if request.method=="POST":
        name = request.POST["name"]
        school = request.POST["school"]
        grade = request.POST["grade"]
        year = request.POST["year"]
        credit = request.POST["credit"]
        income = request.POST["income"]
        impaired = request.POST["impaired"]
        merit = request.POST["merit"]
        major = request.POST["major"]
        regular = request.POST["regular_decision"]
        period= request.POST["period"]
        benefit = request.POST["benefit"]
        spec = request.POST["spec"]
        stype = request.POST["stype"]

        Scholarship.objects.filter(name=name, school=school, grade=grade, year=year, credit=credit, 
        income=income, impaired=impaired, merit=merit, major=major, regular_decision=regular, period=period,
        benefit=benefit, spec=spec, stype=stype).delete()
        return redirect("/manage/")
    else:
        return render(request, "manager.html")
    
def insert_db(request):
    if request.method=="POST":
        name = request.POST["name"]
        school = request.POST["school"]
        grade = request.POST["grade"]
        year = request.POST["year"]
        credit = request.POST["credit"]
        income = request.POST["income"]
        impaired = request.POST["impaired"]
        merit = request.POST["merit"]
        major = request.POST["major"]
        regular = request.POST["regular_decision"]
        period= request.POST["period"]
        benefit = request.POST["benefit"]
        spec = request.POST["spec"]
        stype = request.POST["stype"]

        Scholarship(name=name, school=school, grade=grade, year=year, credit=credit, 
        income=income, impaired=impaired, merit=merit, major=major, regular_decision=regular, period=period,
        benefit=benefit, spec=spec, stype=stype).save()
        return redirect("/manage/")
    else:
        return render(request, "manager.html")

def search_db(request):
    if request.method=="POST":
        search_db=request.POST["searchDB"]

        Scholarship.objects.filter(name=search_db)

        context={
            'Scholarship':Scholarship
        }

        return render(request, "manager.html", context)


        

