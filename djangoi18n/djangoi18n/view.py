# coding:utf-8

from django.http import HttpResponse

from django.utils.translation import ugettext_lazy as _
def hello(request):
    print _("text1")
    print _("text2")
    return HttpResponse("hello world!")
