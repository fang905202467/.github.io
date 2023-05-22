from django.http import HttpResponse


def page_500(request):
    return HttpResponse('服务器正忙，请稍后再试')