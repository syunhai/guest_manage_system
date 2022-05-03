#coding:utf-8
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guest.settings")
django.setup()

from sign.models import Event,Guest

#当前只对guest表进行操作

'''针对 sqllite 操作，批量插入，查找'''
def mul_insert():
    for i in range(20):
            realname = 'test'+ str(i)
            if i < 10:
                phone = '1350000000'+str(i)
            else:
                phone = '135000000'+ str(i)
            email = realname + '@mail.com'
            sign = False
            event_id = 1
            Guest.objects.create(realname=realname,phone=phone,email=email,
                                 sign=sign,event_id=event_id)

if __name__ == '__main__':
    mul_insert()