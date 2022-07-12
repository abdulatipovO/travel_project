from unicodedata import category
from django.shortcuts import render
from django.views import View
from main.models import *
from django.http  import JsonResponse
from django.core.paginator import Paginator

# Create your views here.


class HomePageView(View):
    def get(self,request):
        destination = Direction.objects.all()
        context = {
            "destination":destination,
            }
        return render(request, "index.html",context,)

def change_lang(request):
    lang = request.GET.get('current_lang')
    if lang in ['uz','ru','en']:
        request.session['lang'] = lang

    return JsonResponse({"status":200})




class AboutPageView(View):
    def get(self,request):
        return render(request, 'about.html')

class NewsPageView(View):
    def get(self,request):
        new = News.objects.all()
        category_news = CategoryNews.objects.all()

        paginator = Paginator(new,1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "new":new,
            "category_news":category_news,
            'page_obj':page_obj,
        }
        return render(request, 'news.html',context)


class ContactPageView(View):
    def get(self,request):
        return render(request, 'contact.html')
    
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']
        Contact.objects.create(name=name, email=email, subject=subject, text=msg)
        return render(request, 'contact.html')




class DestinationPageView(View):
    def get(self,request):
        return render(request, 'destinations.html')

def main():
    pass