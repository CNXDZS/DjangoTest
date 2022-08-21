# mysite1/mysite1/views.py
from django.http import HttpResponse
import os
import time
from django.contrib import messages
from loguru import logger
from django.shortcuts import render
from mysite1.sql import MysqlClient
from mysite1.config import note_table

MYSQL_PE = {
    "host": "127.0.0.1",
    # "host": "120.26.93.126",
    "user": "root",
    "passwd": "admin",
    "db": "django",
    "port": 3306,
}


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

    html = '<h1>这是编号为%s的网页</h1>' % (n)
    return HttpResponse(html)


def math_view(request, x, op, y):
    print(1111111)
    print(x)
    print(op)
    print(y)

    x = int(x)  # 小心类型 -> str
    y = int(y)
    result = None
    if op == 'add':
        result = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y

    html = '结果: %s' % (str(result))
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


# def get_userinfo():
#     """
#     获取用户账号密码信息
#     :return: 用户账号密码信息字典
#     """
#     user_info = {}
#     if os.name == 'nt':
#         path_source = r"D:\服务器\mysite1"
#     file_path = os.path.join(path_source,"login_info.txt)")
#     with open(file_path, "r", encoding="utf-8") as f:
#         res = f.readlines()
#     for item in res:
#         item_list = item.split(" ")
#         username = item_list[0]
#         password = item_list[1]
#         user_info[username] = password
#     return user_info

def save_content(title, content):
    """
    本地记录提交的title和content
    :param title: 标题
    :param content: 内容
    :return:
    """
    time_save = time.strftime("%Y-%m-%d %H:%M:%S")
    title_save = title
    content_save = content
    logger.info("开始写入")
    with open("./note.txt", "a+", encoding="utf-8") as f:
        f.write(str(time_save) + ">>>" + title_save + ":" + content_save + "\n")
    logger.success("写入成功")


def record_view(request):
    if request.method == 'GET':
        html = """
        <form method='post' action="/login" {% csrf_token %}>
        姓名:<input type="text" name="username">
        密码:<input type="text" name="password">
        <input type='submit' value='提交'>
        </form>

        """
        return HttpResponse(html)


def login(request):
    if request.method == 'POST':
        post_dict = request.POST
        username = post_dict.get("username")
        password = post_dict.get("password")
        user_info = {"dingyujie": "123456"}
        if user_info.get(username) and user_info[username] == password:
            html = """
            <br>登陆了</br>
                    <form method='post' action="/save" {% csrf_token %}>
        标题:<input type="text" name="title">
        内容:<input type="text" name="content">     
        <input type='submit' value='登陆'>
        </form>
        {% if messages %}
        <script>
            {% for msg in messages %}
                alert('{{ msg.message }}');
            {% endfor %}
        </script>
        {% endif %}
            """
        else:
            html = "<br>没登陆</br>"
        return HttpResponse(html)


def save(request):
    if request.method == 'POST':
        django_client = MysqlClient(MYSQL_PE)
        post_dict = request.POST
        title = post_dict.get("title")
        content = post_dict.get("content")
        django_client.insert(column=["title", "content"], info=([title,content]),table=note_table)
        save_content(title, content)
        messages.success(request, '提交信息完成')
        django_client.close()
        return render(request, "save.html")
    if request.method == 'GET':
        return render(request, "save.html")
