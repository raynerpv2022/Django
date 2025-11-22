# Define Url patterns for Learnings logs.

from django.urls import path # aunque en elprojecto hay un urls.py, es mejor en acda app tener el propio file urls.py
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('',views.index, name="index"),
    path('topics/',views.topics,name='topics'),
    path('topic/<int:topic_id>/', views.topic, name="topic"),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:toppic_id>',views.new_entry,name="new_entry"),
    path('edit_entry/<int:entry_id>', views.edit_entry, name="edit_entry"),
    path("userlist/",views.showuser, name="userlist")
]