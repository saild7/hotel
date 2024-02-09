from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from home.forms import ContactForm, SearchForm
from home.models import ContactMessage, Setting
from room.models import Images, Room


# Create your views here.
def index(request):
    setting=Setting.objects.get(pk=1)
    rooms = Room.objects.all().order_by('id')[:4]#first 4
    context ={'setting':setting,'rooms':rooms}
    return render(request,'index.html',context)

def about(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request,'about.html',context)

def room_details(request,id,slug):
    room=Room.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    context={'room':room,'images':images}
    return render(request,'room-details.html',context)

def search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            max_children=form.cleaned_data['max_children']
            max_adult=form.cleaned_data['max_adult']
            print(max_children)
            rooms=Room.objects.filter(max_adult=max_adult,max_children=max_children)
            print(rooms)
            setting=Setting.objects.get(pk=1)
            context={'setting':setting,'rooms':rooms}
            return render(request,'search_products.html',context)
    return redirect('/')

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage() #create relation with table
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save() #save data to the table
            messages.success(request,"Your message has been sent,Thank you!")
            return redirect('/contact')

    setting=Setting.objects.get(pk=1)
    settings = Setting.objects.get(pk=1)
    form=ContactForm
    context = {'setting': settings,'form':form,'setting':setting}
    return render(request, template_name='contact.html', context=context)

def our_rooms(request):
    setting=Setting.objects.get(pk=1)
    rooms = Room.objects.all().order_by('id')
    context ={'setting':setting,'rooms':rooms}
    return render(request,'our_rooms.html',context)
