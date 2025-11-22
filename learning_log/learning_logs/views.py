from django.shortcuts import render,redirect

from .models import Topic, Entry
from .forms import TopicsForms, EntryForms
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,"learning_logs/index.html")

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_owner(topic.owner,request.user)
    entry = topic.entry_set.order_by('-date_added')
    value = {"topic":topic,"entry":entry}
    return render(request, 'learning_logs/topic.html', value)

@login_required
def new_topic(request):
    
    if request.method != "POST":
        form = TopicsForms()
    else:
        form = TopicsForms(data = request.POST)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.owner = request.user
            newtopic.save()
            return redirect("learning_logs:topics")
    form.fields["text"].widget.attrs["placeholder"] = "Escribe algun texto"
    context = {"form":form}
    return render(request,"learning_logs/new_topic.html",context)

@login_required
def new_entry(request, toppic_id):
    topic = Topic.objects.get(id=toppic_id)
    check_owner(topic.owner,request.user)
    if request.method != 'POST':
        entryForm = EntryForms()
    else:
        
            entryForm = EntryForms(data=request.POST)
            if entryForm.is_valid():
                newEntryForms = entryForm.save(commit=False)
                newEntryForms.topic = topic
                newEntryForms.save()
                return redirect("learning_logs:topic", topic_id=toppic_id)
        

    data = {"topic":topic,"entry":entryForm}
    return render(request,'learning_logs/new_entry.html',data)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    toppic = entry.topic
    check_owner(toppic.owner, request.user)

    if request.method != 'POST':
        entryForm = EntryForms(instance=entry)
    else:
        entryForm = EntryForms(instance=entry, data=request.POST)
        if entryForm.is_valid():
            entryForm.save()
            return redirect("learning_logs:topic", topic_id=toppic.id)
    data = {"topic":toppic, "entry":entry,"entryForm":entryForm}
    return render(request,"learning_logs/edit_entry.html", data)


def showuser(request):
    users = User.objects.all()
    usersDic = {}

    for u in users:
        topic= u.topic_set.all()
        usersDic[u] = [c.text for c in topic]



    data = {"userlist":users, "usersDic":usersDic}
     
    return render(request,"learning_logs/userlist.html",data)

def check_owner(user, owner):
    if user != owner:
        return 
