"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view),
    # 请求 http://127.0.0.1:8000/page1； 交由 views.page_view方法处理
    url(r'^page1$', views.page_view),
    url(r'^page2$', views.page2_view),
    #page3 ... page100
    url(r'^page(\d+)', views.pagen_view),
    #127.0.0.1:8000/123/add/434
    url(r'^(\d+)/(\w{3})/(\d+)', views.math_view),
    #127.0.0.1:8000/person/guoxiaonao/30
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),

    #127.0.0.1:8000/birthday/year/month/day
    url(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})', views.birthday_view),
    #127.0.0.1:8000/birthday/month/day/year
    url(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})', views.birthday_view)




















]
