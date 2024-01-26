from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')
# Create your views here.

def contect(requset):
    return render(requset, 'pages/qna.html')