# mysite1/mysite1/views.py
from django.http import HttpResponse


# def page_view(request):
#
#     html = '<h1>这是第一个页面</h1>'
#     return HttpResponse(html)

def index_view(request):

    html = '<h1>这是主页</h1>'
    return HttpResponse(html)

def page_view(request):

    html = '<h1>这是编号为1的网页</h1>'
    return HttpResponse(html)


def page2_view(request):

    html = '<h1>这是编号为2的网页</h1>'
    return HttpResponse(html)

def pagen_view(request, n):

    print(1111111)
    print(type(n))

    html = '<h1>这是编号为%s的网页</h1>'%(n)
    return  HttpResponse(html)

def math_view(request, x, op, y):

    print(1111111)
    print(x)
    print(op)
    print(y)

    x = int(x)  #小心类型 -> str
    y = int(y)
    result = None
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y

    html = '结果: %s'%(str(result))
    return HttpResponse(html)


# def person_view(request, **kwargs):
#
#     s = str(kwargs)
#     return HttpResponse(s)

def person_view(request, name, age):

    s = '姓名： ' + name
    s += ' 年龄: ' + age
    return HttpResponse(s)


def birthday_view(request, y, m, d):

    if request.method == 'GET':
        your_ip = request.META['REMOTE_ADDR']
        print(your_ip)
        html = '生日: ' + y + '年' + m + '月' + d + '日 ' + your_ip
        return HttpResponse(html)

    elif request.method == 'POST':
        pass






















