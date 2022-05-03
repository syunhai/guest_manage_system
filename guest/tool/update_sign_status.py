#coding:utf-8
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guest.settings")
django.setup()

from sign.models import Guest

def singal_change(phone, eid, status=True):
    res = Guest.objects.get(event_id=eid, phone=phone)
    if res is not None:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign=status)
        result = Guest.objects.get(event_id=eid, phone=phone)
        print(result.sign)
    else:
        raise ValueError (phone,'not choose this event')

if __name__ == '__main__':
    singal_change(phone='15110000000',eid='1',status=False)