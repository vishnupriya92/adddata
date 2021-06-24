from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Topic,Webpage
# Create your views here.
def form1(request):
    if request.method=="POST":
        #print(request.POST)
        print(request.POST.get("name"))
        print(request.POST.get("emailid"))
        print(request.POST.get("phno"))
        print(request.POST.get("gender"))
    return render(request,"form1.html")

def form2(request):
    return render(request,"form2.html")

def resp(request):
    #return HttpResponse("control came to resp")
    data={}
    if request.method=="POST":
        data=dict(request.POST)
        data.pop("csrfmiddlewaretoken")
    return render(request,"resp.html",{'data':data})

def add_topic(request): 
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.create(top_name=topic)
        t.save()
        return HttpResponse("<h1>Topic added successfully")
    return render(request,"create_topic.html")

def create_webpage(request):
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",{"topics":topics})

def add_webpage(request):
    topic=request.POST.get("topic")
    name=request.POST.get("name")
    url=request.POST.get("url")
    t=Topic.objects.get_or_create(top_name=topic)[0]
    w=Webpage.objects.create(topic=t,name=name,url=url)
    t.save()
    w.save()
    return HttpResponse("webpage added successsfully")















