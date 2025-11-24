from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns =[
    path("",views.index, name='index'),
    path('blog/',views.blog, name="blog"),
    path('new_thema/',views.new_thema, name='new_thema'),
    path('thema/<int:id_thema>', views.thema, name='thema'),
    path('new_subthema/<int:id_thema>', views.new_subthema, name="new_subthema"),
    path('edit_thema/<int:id_subthema>', views.edit_subthema,name="edit_subthema"),
    path('userlist/',views.showuser,name="userlist"),

]