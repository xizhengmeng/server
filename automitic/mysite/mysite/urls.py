"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from learn import views as learn_views  # new
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
               url(r'next', learn_views.nextPage),  # new
               url(r'^$', learn_views.home,name='home'),  # new
               url(r'^admin/', admin.site.urls),
               url(r'callPython', learn_views.compute),  # new
               url(r'add', learn_views.compute),  # new
               url(r'uicreate', learn_views.uicreate),
               url(r'ajaxcreateui', learn_views.createui),
               url(r'ajaxsendMail', learn_views.sendMails),
               url(r'jsonFormatClick1', learn_views.jsonFormat1),
               url(r'jsonFormatClick2', learn_views.jsonFormat2),
               url(r'interfaceTestClick', learn_views.interfaceTest),
               url(r'blockClick', learn_views.blockClickview),
               url(r'webserver', learn_views.webserver),
               url(r'fullnewweb', learn_views.webserverfullre),
               url(r'url1', learn_views.getUrl1),
               url(r'url2', learn_views.getUrl2),  # new
               url(r'url3', learn_views.getUrl3),
               url(r'url4', learn_views.getUrl4),
               url(r'url5', learn_views.getUrl5),  # new
               url(r'url6', learn_views.getUrl6),
               url(r'url7', learn_views.getUrl7),
               url(r'getcontent', learn_views.getcontentstring),
               url(r'writecontent', learn_views.writestring),
               url(r'getforderlist', learn_views.checkfilelist),
               url(r'createforder', learn_views.createforder),
               url(r'jinkens', learn_views.gotojinkens),
               url(r'gotogit', learn_views.gotogitjdjr),
               url(r'packageAndroid', learn_views.packAndroid),
               url(r'suggest', learn_views.suggest),
               url(r'writesuggest', learn_views.writesuggest),

               ]

# ... the rest of your URLconf goes here ...
urlpatterns += staticfiles_urlpatterns()
