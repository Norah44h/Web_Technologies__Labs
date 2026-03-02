from django.http import HttpResponse
from django.shortcuts import render


#def index(request):  #http://127.0.0.1:8000/
#    return HttpResponse("Hello, world!")

#def index(request):
    #name = request.GET.get("name") or "world!"
    #return HttpResponse("Hello, " + name)

#def index(request):
    #return render(request, "bookmodule/index.html")  #http://127.0.0.1:8000/

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})  #http://127.0.0.1:8000?name=Norah

def index2(request, val1 = 0):
    return HttpResponse("value1 = " + str(val1))

