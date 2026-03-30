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


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

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

def search_view(request):
    return render(request, 'bookmodule/search.html')


def list_books(request):
    # جلب كل الكتب من الدالة التي أنشأناها يدوياً
    all_books = __getBooksList()

    # إرسال كل الكتب لملف list_books.html
    return render(request, 'bookmodule/list_books.html', {'books': all_books})

def __getBooksList():
    return [
        {'id': 1, 'title': 'تأملات يومية', 'author': 'نورة محمد', 'category': 'رواية'},
        {'id': 2, 'title': 'ماذا لو فتح الباب', 'author': 'كاتب أدبي', 'category': 'رواية أدبية'},
        {'id': 3, 'title': 'Silent Whispers', 'author': 'Unknown', 'category': 'فلسفة وتأملات'},
        {'id': 4, 'title': 'Machines That Matter', 'author': 'Tech Expert', 'category': 'تطوير ذات'}
    ]


def search_view(request):
    if request.method == "POST":
        # 1. استقبال الكلمة وتحويلها لحروف صغيرة (للبحث بالإنجليزية بدقة)
        string = request.POST.get('keyword').lower()

        # 2. التأكد من الخيارات المختارة (العنوان أو المؤلف)
        # لاحظي أن الأسماء 'option1' و 'option2' يجب أن تطابق الـ name في ملف search.html
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # 3. جلب قائمة كتبكِ الخاصة
        books = __getBooksList()
        newBooks = []

        # 4. محرك البحث (الفلترة)
        for item in books:
            contained = False
            # البحث في العنوان
            if isTitle and string in item['title'].lower():
                contained = True
            # البحث في المؤلف (إذا لم يجد في العنوان أو إذا اختار المستخدم المؤلف أيضاً)
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            # إذا وجدنا تطابقاً، نضيف الكتاب لقائمة النتائج
            if contained:
                newBooks.append(item)

        # 5. إرسال النتائج لصفحة bookList.html لعرضها
        return render(request, 'bookmodule/list_books.html', {'books': newBooks})

    # إذا كان الطلب فتح الصفحة لأول مرة (GET)
    return render(request, 'bookmodule/search.html')

