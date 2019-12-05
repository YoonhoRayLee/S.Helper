from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q, F, Subquery
from django.contrib import auth
from accounts.models import scholarship_info
from manager.models import Scholarship, Contest, User_Contest, Events, User_Scholarship, Notice
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
#from django.db.models.manager import objects

def signup(request):
    if request.method == "POST":
        uid = request.POST["username"]
        is_user = User.objects.filter(username=uid)
        if is_user.count() != 0:
            messages.info(request, '중복되는 아이디가 존재합니다!')
            return redirect('signup')
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

def check(request):
    return render(request, 'check.html')

def notice(request):
    notice_table = Notice.objects.all()
    context = {
        'notice_table':notice_table,
    }
    return render(request, 'notice.html', context)

def notice_result(request):
    if request.method=="GET":
        title = request.GET.get('delete', '')
        Notice.objects.filter(title=title).delete()
        messages.info(request, '공지사항을 삭제했습니다!')
        return redirect('/notice/')
    else:
        if request.method=="POST":
            nid = request.POST['nid']
            notice_table = Notice.objects.filter(id = nid)
            notice_table.update(hit=F('hit')+1)
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
            messages.info(request, '아이디/패스워드가 틀렸습니다!')
            return render(request, 'accounts/login.html')

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
    uid = request.user.username
    is_user_in_db = scholarship_info.objects.filter(uid=uid)
    if is_user_in_db.count() == 0:
        return redirect('/check/')
    else:
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
        return render(request, 'result_contest.html')

def result(request):
    uid = request.user.username
    is_user_in_db = scholarship_info.objects.filter(uid=uid)
    if is_user_in_db.count() == 0:
        return redirect('/check/')
    else:
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

def already(request):
    return render(request, 'already.html')

def add_db(request):
    if request.method == "POST": 
        if request.POST.get('scholarship', ''):
            num1 = request.POST.get('scholarship', '')
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
            messages.info(request, '장학정보를 등록하였습니다!')
            return redirect("/add_db/")
        else:
            num2 = request.POST.get('contest', '')
            company = request.POST["company"]
            Ctype = request.POST["Ctype"]
            title = request.POST["title"]
            content = request.POST["content"]
            sdate = request.POST["sdate"]
            edate = request.POST["edate"]
            Contest(company=company, Ctype=Ctype, title=title, content=content, sdate=sdate, 
            edate=edate).save()
            messages.info(request, '공모전정보를 등록하였습니다!')
            return redirect("/add_db/")
    else:
        return render(request, "add_db.html")

#@login_required
def register(request):
    uid = request.user.username
    is_user_in_db = scholarship_info.objects.filter(uid=uid)
    if is_user_in_db.count() == 0:
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

            scholarship_info(uid=username, income=income, grade=credit, year=grade,
                        credit=taken_credit, school=univ_name, major=department_stype,
                        impaired=disability, merit=national_merit, regular_decision=apply_stype).save()
            return redirect('/index/')
        else:
            return render(request, 'register.html')
    else:
        return redirect('already')

def delete_user(request):
    if request.method == "POST":
        uid = request.user.username
        user_db = scholarship_info.objects.filter(uid = uid).delete()
        request.user.delete()
        messages.info(request, '회원탈퇴를 완료하였습니다!')
        return redirect('/index/')
    else:
        return render(request, 'delete_user.html')

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
        uid = request.user.id
        selectedContest = []
        selectedScholarship = []
        for user_contest in User_Contest.objects.filter(user_id = uid):
            selectedContest.append(Contest.objects.get(id=user_contest.contest_id))
        for user_scholarship in User_Scholarship.objects.filter(user_id = uid):
            selectedScholarship.append(Scholarship.objects.get(id=user_scholarship.scholarship_id)) 

        # result_table = Contest.objects.filter(id=Subquery(User_Contest.objects.filter(user_id = uid).order_by('contest_id').values('contest_id')[:1])).values('title', 'sdate', 'edate')
        print(selectedContest)
        context = {
            'result_table' : selectedContest,
            'result_table2' : selectedScholarship,
        }
        return render(request, 'mypage.html', context)

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    if not user_passes_test:
        return redirect('/index/')

    Scholarship_list = Scholarship.objects.all()
    Contest_list = Contest.objects.all()
    paginator = Paginator(Scholarship_list, 10)
    paginator2 = Paginator(Contest_list, 10)
    page = request.GET.get('page', default=1)
    page2 = request.GET.get('page2', default=1)
    searchDB = request.GET.get("searchDB")
    searchDB2 = request.GET.get("searchDB2")
    try:
        scholarships = paginator.page(page)
        contests = paginator2.page(page2)
    except PageNotAnInteger:
        scholarships = paginator.page(1)
        contests = paginator2.page(1)
    except EmptyPage:
        scholarships = paginator.page(paginator.num_pages)
        contests = paginator2.page(paginator2.num_pages)

    if request.method=="POST":
        if request.POST.get('sid', ''):
            sid = request.POST.get('sid', '')
            delete_scholarship = Scholarship.objects.get(id=sid)
            delete_scholarship.delete()
            messages.info(request, '해당 장학을 삭제 했습니다!')
        else:
            cid = request.POST.get('cid', '')
            delete_contest = Contest.objects.get(id=cid)
            delete_contest.delete()
            messages.info(request, '해당 공모전을 삭제 했습니다!')

    data = { 'scholarships':scholarships, "page": page , 'contests':contests, "page2":page2}

    if searchDB:
        search_scholarship = Scholarship.objects.filter(name__contains=searchDB)
        data['result_table'] = search_scholarship
    if searchDB2:
        search_contest = Contest.objects.filter(title__contains=searchDB2)
        data['result_table2'] = search_contest

    return render(request, 'manage.html', data)

    