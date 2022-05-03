from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
    #return HttpResponse('hello,django word')
    return render(request,'index.html')
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        #if username == 'admin' and password == 'admin123':
        if user is not None:
            auth.login(request,user)
            res = HttpResponseRedirect('/event_manage/')
            #res.set_cookie('user',username,600)
            request.session['user'] = username
            return res
        else:
            return render(request,'index.html',{'error':'username or password error'})
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user','')
    event_list = Event.objects.all()
    return render(request,'event_manage.html',{'user':username,'events':event_list})
@login_required
def guest_manage(request):
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,'guest_manage.html',{'user':username,'guests':contacts})
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    table = request.GET.get('table','')
    if table == 'event':
        event_list = Event.objects.filter(name__contains = search_name)
        return render(request, 'event_manage.html', {'user': username, 'events': event_list})
    elif table == 'guest':
        guest_list = Guest.objects.filter(realname__contains = search_name)
        return render(request, 'guest_manage.html', {'user': username, 'guests': guest_list})
@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event, id = eid)
    return render(request, 'sign_index.html', {'event':event})

def sign_index_action(request, eid):
    event = get_object_or_404(Event, id = eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone is not exsisted'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return  render(request,'sign_index.html',{'event':event,'hint':'phone or event not refer'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'user has sign in'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'sign in success','user':result})

def logout(request):
    auth.logout(request)
    res = HttpResponseRedirect('/index/')
    return res