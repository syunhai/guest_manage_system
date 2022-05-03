import requests
'''在开发框架中启动csrf检测，post接口测试需要提供csrf_token，且涉及请求上下
文关联，post测试中使用session()'''
def gtest():
    url = 'http://127.0.0.1:8000/api/add_event/'
    params = {'e': 'e123', 'g': 2}
    #data = {'username':'admin','password':'admin123456'}
    data = {'eid': '1', 'name': 'hongmi1'}
    res = requests.get('http://127.0.0.1:8000/index/')

    #print(res.text)
    #print(res.headers)
    print(res.cookies['csrftoken'])
    data['csrfmiddlewaretoken'] = res.cookies['csrftoken']
    print(data)
    res = requests.post(url,data=data)
    print(res.text)
    print(res.url)

def ptest():
    #url = 'http://127.0.0.1:8000/login_action/'
    url = 'http://127.0.0.1:8000/api/add_event/'
    params = {'e': 'e123', 'g': 2}
    #data = {'username':'admin','password':'admin123456'}
    data = {'eid': '1', 'name': 'hongmi1'}
    client = requests.session()
    res = client.get('http://127.0.0.1:8000/index/')
    # print(client.text)
    print(res.headers)
    print(res.cookies)
    data['csrfmiddlewaretoken'] = res.cookies['csrftoken']
    print(data)
    res = client.post(url, data=data)
    print(res.text)
    print(res.url)
if __name__ == '__main__':
    #gtest()  #不成功,只能使用session解决csrf  使用会话
    ptest()