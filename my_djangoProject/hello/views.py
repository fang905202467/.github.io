from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse, HttpResponseRedirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse


def hello_world(request):
    return HttpResponse('hello world')

def hello_china(request):
    print(reverse('hello_world'))
    return HttpResponse('hello china')

def hello_html(request):
    """响应html内容"""
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)

def article_list(request,month):
    return HttpResponse('article:{}'.format(month))

def search(request):
    name = request.GET.get('name','')
    print(name)
    return HttpResponse('查询成功')

def render_str(request):
    templ_name = 'hello/index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)

def render_html(request):
    return render(request,'index.html')

def http_request(request):
    """请求练习"""
    # 1.请求方式
    print(request.method)
    # 2.请求头信息
    headers = request.META
    print(headers)
    ua = request.META.get('HTTP_USER_AGENT',None)
    print(ua)
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.headers['user-agent'])
    # 3.获取请求参数
    name = request.GET.get('name',None)
    print(name)
    return HttpResponse('响应')

def http_response(request):
    """响应练习"""
    # resp = HttpResponse('响应内容',status=201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp
    # 响应json
    # user_info = {
    #     'name' : '张三',
    #     'age' : 34
    # }
    # return JsonResponse(user_info)

    # 响应文件
    return FileResponse(open('hello/imgs/tupian.png','rb'))

def no_data_404(request):
    """404页面"""
    return HttpResponse('404')

def article_dateil(request,article_id):
    """
    文章详情，id时从1000开始的整数
    """
    if article_id < 1000:
        return HttpResponseRedirect('/hello/404/')
    return HttpResponse('文章{}的内容'.format(article_id))