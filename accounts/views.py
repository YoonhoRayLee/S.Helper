from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import auth
from accounts.models import scholarship_info
from manager.models import Scholarship, Contest, Events, User_Contest, User_Scholarship, Notice
from django.contrib import messages
from django.db.models import F
#from django.db.models.manager import objects

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            username = request.POST["username"]
            password = request.POST["password1"]
            email = request.POST["email"]

            user = User.objects.create_user(username, email, password)
            user.save()
            auth.login(request, user)
            return redirect('/index/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')

def notice(request):
    notice_table = Notice.objects.all()
    context = {
        'notice_table':notice_table,
    }
    return render(request, 'notice.html', context)

def notice_result(request):
    if request.method == "POST":
        nid = request.POST['nid']     
        notice_table = Notice.objects.filter(id = nid)
        context = {
            'notice_table':notice_table,
        }
        return render(request, 'notice_result.html', context)
    else:
        return render(request, 'notice_result.html', context)
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        #id, pw 없을 때 팝업

        if user is not None:
            auth.login(request, user)
            return redirect('/index/')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'}) #!!!!!!!!!!!!

    else:
        return render(request, 'accounts/login.html')

def calendar(reqeust):
    return render(reqeust, 'calendar.html')

def logout(request):
    auth.logout(request)
    return redirect('/index/')

def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
      
        is_notice_db = Notice.objects.filter(title = title, content = content)
        if is_notice_db.count() == 0:
            notice_db = Notice(title = title, content = content)
            notice_db.save()
            messages.info(request, '공지사항을 작성했습니다!')
            return redirect('/notice/')
        else:
            messages.info(request, '이미 존재하는 공지사항입니다!')
            return redirect('/notice/')

        return redirect('/contest1/')
    else:
        return render(request, 'form.html')

def about(request):
    return render(request, 'about.html')
    
def result_contest(request):
    if request.method == "POST":
        if request.POST.get('광고', '') == '광고':
            return render(request, 'contest1.html')
        else:
            return render(request, 'result_contest.html')
        if request.POST.get('과학', '') == '과학':
            return render(request, 'contest2.html')
        else:
            return render(request, 'result_contest.html')

        if request.POST.get('디자인', '') == '디자인':
            return render(request, 'contest3.html')
        else:
            return render(request, 'result_contest.html')

        if request.POST.get('UCC', '') == 'UCC':
            return render(request, 'contest4.html')
        else:
            return render(request, 'result_contest.html')
    else:
        return render(request, 'result_contest.html')

def result(request):
    if request.method == "POST":
        if request.POST.get('성적장학', '') == '성적':
            return render(request, 'service1.html')
        else:
            return render(request, 'result.html')
        if request.POST.get('복지장학', '') == '복지':
            return render(request, 'service2.html')
        else:
            return render(request, 'result.html')

        if request.POST.get('개인활동장학', '') == '개인활동':
            return render(request, 'service3.html')
        else:
            return render(request, 'result.html')

        if request.POST.get('특수장학', '') == '특수':
            return render(request, 'service4.html')
        else:
            return render(request, 'result.html')
    else:
        return render(request, 'result.html')

def need_login(request):
    return render(request, 'need_login.html')

def contest1(request):
    if request.method == "POST":
        uid = request.user.id
        cid = request.POST['cid']
      
        is_user_in_db = User_Contest.objects.filter(user_id = uid, contest_id = cid)
        if is_user_in_db.count() == 0:
            user_contest_db = User_Contest(user_id = uid, contest_id = cid)
            user_contest_db.save()
            messages.info(request, '해당 공모전을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 공모전입니다!')
            return redirect('/contest1/')

        return redirect('/contest1/')
    else:
        contest_table = Contest.objects.filter(Ctype='광고')
        context = {
            'contest_table':contest_table,
        }
        return render(request, 'contest1.html', context)

def contest2(request):
    if request.method == "POST":
        uid = request.user.id
        cid = request.POST['cid']
      
        is_user_in_db = User_Contest.objects.filter(user_id = uid, contest_id = cid)
        if is_user_in_db.count() == 0:
            user_contest_db = User_Contest(user_id = uid, contest_id = cid)
            user_contest_db.save()
            messages.info(request, '해당 공모전을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 공모전입니다!')
            return redirect('/contest2/')

        return redirect('/contest2/')
    else:
        contest_table = Contest.objects.filter(Ctype='광고')
        context = {
            'contest_table':contest_table,
        }
        return render(request, 'contest2.html', context)

def contest3(request):
    if request.method == "POST":
        uid = request.user.id
        cid = request.POST['cid']
      
        is_user_in_db = User_Contest.objects.filter(user_id = uid, contest_id = cid)
        if is_user_in_db.count() == 0:
            user_contest_db = User_Contest(user_id = uid, contest_id = cid)
            user_contest_db.save()
            messages.info(request, '해당 공모전을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 공모전입니다!')
            return redirect('/contest3/')

        return redirect('/contest3/')
    else:
        contest_table = Contest.objects.filter(Ctype='광고')
        context = {
            'contest_table':contest_table,
        }
        return render(request, 'contest3.html', context)

def contest4(request):
    if request.method == "POST":
        uid = request.user.id
        cid = request.POST['cid']
      
        is_user_in_db = User_Contest.objects.filter(user_id = uid, contest_id = cid)
        if is_user_in_db.count() == 0:
            user_contest_db = User_Contest(user_id = uid, contest_id = cid)
            user_contest_db.save()
            messages.info(request, '해당 공모전을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 공모전입니다!')
            return redirect('/contest4/')

        return redirect('/contest4/')
    else:
        contest_table = Contest.objects.filter(Ctype='광고')
        context = {
            'contest_table':contest_table,
        }
        return render(request, 'contest4.html', context)

def service1(request):
    if request.method == "POST":
        uid = request.user.id
        sid = request.POST['sid']
      
        is_user_in_db = User_Scholarship.objects.filter(user_id = uid, scholarship_id = sid)
        if is_user_in_db.count() == 0:
            user_scholarship_db = User_Scholarship(user_id = uid, scholarship_id = sid)
            user_scholarship_db.save()
            messages.info(request, '해당 장학을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 장학입니다!')
            return redirect('/service1/')

        return redirect('/service1/')
    else:
        username = request.user.username
        
        user_info = get_object_or_404(scholarship_info, uid=username)
        temp_dict = user_info.__dict__
        school_name = temp_dict["school"]
        grade_value = temp_dict["grade"]
        year_value = temp_dict["year"]
        credit_value = temp_dict["credit"]
        income_value = temp_dict["income"]
        impaired_value = temp_dict["impaired"]
        merit_value = temp_dict["merit"]
        major_value = temp_dict["major"]
        regular_decision_value = temp_dict["regular_decision"]

        result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='성적')

        context = {
            'result_table': result_table,
        }
        return render(request, 'service1.html', context)

def service2(request):
    if request.method == "POST":
        uid = request.user.id
        sid = request.POST['sid']
      
        is_user_in_db = User_Scholarship.objects.filter(user_id = uid, scholarship_id = sid)
        if is_user_in_db.count() == 0:
            user_scholarship_db = User_Scholarship(user_id = uid, scholarship_id = sid)
            user_scholarship_db.save()
            messages.info(request, '해당 장학을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 장학입니다!')
            return redirect('/service2/')

        return redirect('/service2/')
    else:
        username = request.user.username
        
        user_info = get_object_or_404(scholarship_info, uid=username)
        temp_dict = user_info.__dict__
        school_name = temp_dict["school"]
        grade_value = temp_dict["grade"]
        year_value = temp_dict["year"]
        credit_value = temp_dict["credit"]
        income_value = temp_dict["income"]
        impaired_value = temp_dict["impaired"]
        merit_value = temp_dict["merit"]
        major_value = temp_dict["major"]
        regular_decision_value = temp_dict["regular_decision"]

        result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='복지')

        context = {
            'result_table': result_table,
        }
        return render(request, 'service2.html', context)

def service3(request):
    if request.method == "POST":
        uid = request.user.id
        sid = request.POST['sid']
      
        is_user_in_db = User_Scholarship.objects.filter(user_id = uid, scholarship_id = sid)
        if is_user_in_db.count() == 0:
            user_scholarship_db = User_Scholarship(user_id = uid, scholarship_id = sid)
            user_scholarship_db.save()
            messages.info(request, '해당 장학을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 장학입니다!')
            return redirect('/service3/')

        return redirect('/service3/')
    else:
        username = request.user.username
        user_info = get_object_or_404(scholarship_info, uid=username)
        temp_dict = user_info.__dict__
        school_name = temp_dict["school"]
        grade_value = temp_dict["grade"]
        year_value = temp_dict["year"]
        credit_value = temp_dict["credit"]
        income_value = temp_dict["income"]
        impaired_value = temp_dict["impaired"]
        merit_value = temp_dict["merit"]
        major_value = temp_dict["major"]
        regular_decision_value = temp_dict["regular_decision"]

        result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='개인활동')

        context = {
            'result_table': result_table,
        }
        return render(request, 'service3.html', context)

def service4(request):
    if request.method == "POST":
        uid = request.user.id
        sid = request.POST['sid']
      
        is_user_in_db = User_Scholarship.objects.filter(user_id = uid, scholarship_id = sid)
        if is_user_in_db.count() == 0:
            user_scholarship_db = User_Scholarship(user_id = uid, scholarship_id = sid)
            user_scholarship_db.save()
            messages.info(request, '해당 장학을 찜 했습니다!')
        else:
            messages.info(request, '이미 찜한 장학입니다!')
            return redirect('/service4/')

        return redirect('/service4/')
    else:
        username = request.user.username
        user_info = get_object_or_404(scholarship_info, uid=username)
        temp_dict = user_info.__dict__
        school_name = temp_dict["school"]
        grade_value = temp_dict["grade"]
        year_value = temp_dict["year"]
        credit_value = temp_dict["credit"]
        income_value = temp_dict["income"]
        impaired_value = temp_dict["impaired"]
        merit_value = temp_dict["merit"]
        major_value = temp_dict["major"]
        regular_decision_value = temp_dict["regular_decision"]

        result_table = Scholarship.objects.filter(school=school_name).filter(Q(grade__lte=grade_value)|Q(grade__isnull=True)).filter(Q(year=year_value)|Q(year__isnull=True)).filter(Q(credit__lte=credit_value)|Q(credit__isnull=True)).filter(Q(income__gte=income_value)|Q(income__isnull=True)).filter(Q(impaired=impaired_value)|Q(impaired__isnull=True)).filter(Q(merit=merit_value)|Q(merit__isnull=True)).filter(Q(major=major_value)|Q(major__isnull=True)).filter(Q(regular_decision=regular_decision_value)|Q(regular_decision__isnull=True)).filter(stype='특수')

        context = {
            'result_table': result_table,
        }
        return render(request, 'service4.html', context)

def is_admin(request):
    return render(request, 'is_admin.html')


#@login_required
def register(request):
    if request.method == "POST":
        username = request.user.username
        income = request.POST['소득분위']
        credit = request.POST['성적정보']
        grade = request.POST['학년']
        taken_credit = request.POST['이수학점']
        univ_name = request.POST['college']
        department_stype = request.POST['지원계열']
        disability = request.POST['장애여부']
        national_merit = request.POST['보훈']
        apply_stype = request.POST['입학유형']

        is_user_in_db = scholarship_info.objects.filter(uid=username)
        if is_user_in_db.count() == 0:
            scholarship_info(uid=username, income=income, grade=credit, year=grade,
                            credit=taken_credit, school=univ_name, major=department_stype,
                            impaired=disability, merit=national_merit, regular_decision=apply_stype).save()
        else:
            messages.info(request, 'You already registered your scholarship information')
            return redirect('/register/')

        return redirect('/index/')
    else:
        return render(request, 'register.html')

def mypage(request):
    if request.method == "POST":
        username = request.user.username
        n_income = request.POST['소득분위']
        n_grade = request.POST['성적정보']
        n_year = request.POST['학년']
        n_credit = request.POST['이수학점']
        n_school = request.POST['college']
        n_major = request.POST['지원계열']
        n_impaired = request.POST['장애여부']
        n_merit = request.POST['보훈']
        n_regular_decision = request.POST['입학유형']
        user_info = get_object_or_404(scholarship_info, uid=username)
        temp_dict = user_info.__dict__
        income = temp_dict["income"]
        grade = temp_dict["grade"]
        year = temp_dict["year"]
        credit = temp_dict["credit"]
        school = temp_dict["school"]
        major = temp_dict["major"]
        impaired = temp_dict["impaired"]
        merit = temp_dict["merit"]
        regular_decision = temp_dict["regular_decision"]
        will_be_modified = scholarship_info.objects.filter(income=income, grade=grade, year=year, credit=credit, school=school, major=major, impaired=impaired, merit=merit, regular_decision=regular_decision )
        modified_table = will_be_modified.update(income=n_income, grade=n_grade, year=n_year, credit=n_credit, school=n_school, major=n_major, impaired=n_impaired, merit=n_merit, regular_decision=n_regular_decision)
        return redirect('/index/')
    else:
        return render(request, 'mypage.html')
