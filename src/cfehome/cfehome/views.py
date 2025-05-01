
import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir=pathlib.Path(__file__).resolve().parent
print(this_dir)
def home_page_view(request,*args,**kwargs):
    # queryset=PageVisit.objects.all()
    # page_qs=PageVisit.objects.filter(path=request.path)
    # my_title="MY_PAGE"
    # html_template="home.html"
    # my_context={
    #     "page_title":my_title,
    #     "queryset":queryset.count(),
    #     "percent":page_qs.count()*100.0/queryset.count(),
    #     "total_visit_count":page_qs.count()
    # }
    # path=request.path
    # print("visit:",path)
   
    # PageVisit.objects.create(path=request.path)
    # # html=""
    # # html_file_path=this_dir/"home.html"
    # # html_=html_file_path.read_text()
    # return render(request,html_template,my_context)


    # # return HttpResponse("<h1> hellow world</h1>")
    return about_view(request,*args,**kwargs)


def about_view(request,*args,**kwargs):
    queryset=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    try: 
        percent=(page_qs.count()*100.0/queryset.count())
    except:
        percent=0
    my_title="MY_PAGE"
    html_template="home.html"
    my_context={
        "page_title":my_title,
        "queryset":queryset.count(),
        "percent":percent,
        "total_visit_count":page_qs.count()
    }
    path=request.path
    print("visit:",path)
   
    PageVisit.objects.create(path=request.path)
    # html=""
    # html_file_path=this_dir/"home.html"
    # html_=html_file_path.read_text()
    return render(request,html_template,my_context)


    # return HttpResponse("<h1> hellow world</h1>")


def my_old_home_page_view(request,*args,**kwargs):
    my_title="MY_PAGE"
    my_context={
        "page_title":my_title
    }
    html="""
    """
    html_file_path=this_dir/"home.html"
    html_=html_file_path.read_text()
    return HttpResponse(html_)
