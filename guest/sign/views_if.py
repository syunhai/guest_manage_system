#coding:utf-8
from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist

#添加发布会接口
def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status':'10021','message':'parameter error'})
    res = Event.objects.get(id=eid)
    if res:
        return JsonResponse({'status':'10022','message':'event already exists'})
    res = Event.objects.filter(name=name)
    if res:
        return JsonResponse({'status':'10023','message':'the same name is used'})
    if status == '':
        status =0
    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error, YYYY-MM-DD HH:MM:SS'
        return JsonResponse({'status':'10024','message':error})
    return JsonResponse({'status':200,'message':'add event success'})

#查询发布会信息
def get_event_list(request):
    eid = request.GET.get('edi','')
    name = request.GET.get('name','')

    if eid == '' and name == '':
        return JsonResponse({'status':'10021','message':'parameter is empty'})
    if eid != '':
        event = {}
        try:
            res = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'10022','message':'query result is empty'})
        else:
            event['name'] = res.name
            event['limit'] = res.limit
            event['status'] = res.status
            event['address'] = res.address
            event['start_time'] = res.start_time
            return JsonResponse({'status':'200','message':'success','data':event})
    if name != '':
        data = []
        res = Event.objects.filter(name__contains=name)
        if res:
            for r in res:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                data.append(event)
            return JsonResponse({'status':'200','message':'success','data':data})
        else:
            return JsonResponse({'status':'10022','message':'query result is empty'})

