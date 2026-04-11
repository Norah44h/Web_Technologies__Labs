from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


#def index(request):  #http://127.0.0.1:8000/
#    return HttpResponse("Hello, world!")

#def index(request):
    #name = request.GET.get("name") or "world!"
    #return HttpResponse("Hello, " + name)

#def index(request):
    #return render(request, "bookmodule/index.html")  #http://127.0.0.1:8000/

#def index(request):
    #name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html", {"name": name})  #http://127.0.0.1:8000?name=Norah

def index2(request, val1 = 0):
    return HttpResponse("value1 = " + str(val1))

def index(request):
    return render(request, "bookmodule/index.html")

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_view(request):
    return render(request, 'bookmodule/links.html')

def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def list_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': all_books})

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = Book.objects.all()
        newBooks = []

        for item in books:
            contained = False
            #  هنا استخدمنا item.title وليس ['title'] لأنها كائنات من الداتابيس
            if isTitle and string in item.title.lower():
                contained = True
            if not contained and isAuthor and string in item.author.lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    return render(request, 'bookmodule/search.html')

def simple_query(request):
    # جلب الكتب التي يحتوي عنوانها على كلمة 'and' (تجاهل حالة الأحرف)
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    # الفلترة هنا دقيقة جداً حسب طلب اللاب
    mybooks = Book.objects.filter(author__isnull=False)\
                         .filter(title__icontains='d')\
                         .filter(edition__gte=2)\
                         .exclude(price__lte=100)
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')



