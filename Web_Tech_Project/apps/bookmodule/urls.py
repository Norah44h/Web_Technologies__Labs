from django.urls import path
from . import views

urlpatterns = [
    #path('index2/', views.index2, name="index2"),
    path('', views.index, name="books.index"),
    #path('list_books/', views.list_all_books, name="list_all_books"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_view, name='books.html5_links'),
    path('html5/text/formatting', views.formatting_view, name='books.html5_formatting'),
    path('html5/listing', views.listing_view, name='books.html5_listing'),
    path('html5/tables', views.tables_view, name='books.html5_tables'),
    path('search', views.search_view, name='books.search'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('list_books/', views.list_all_books, name="list_all_books"),
    path('lab8/task1/', views.task1, name="lab8_task1"),
    path('lab8/task2/', views.task2, name="lab8_task2"),
    path('lab8/task3/', views.task3, name="lab8_task3"),
    path('lab8/task4/', views.task4, name="lab8_task4"),
    path('lab8/task5/', views.task5, name="lab8_task5"),
    path('lab8/task7/', views.task7, name="lab8_task7"),
]