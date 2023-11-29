from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Core.models import Banner,Gallery_Image,Review,Enquiry,Partners,Event

# Create your views here.

def home(request):
    mobile_banners = Banner.objects.filter(Banner_Type='Mobile')
    system_banners = Banner.objects.filter(Banner_Type='System')
    images = Gallery_Image.objects.all().order_by('-id')[:6]
    reviews = Review.objects.all().order_by('-id')[:6]
    partners = Partners.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-Date')[:3]

    context = {
        'mobile_banners' : mobile_banners,
        'system_banners' : system_banners,
        'images' : images,
        'reviews' : reviews,
        'partners' : partners,
        'events' : events
    }
    return render(request,'Frontpage/index.html',context)

def about(request):
    reviews = Review.objects.all().order_by('-id')
    partners = Partners.objects.all().order_by('-id')

    context = {
        'reviews' : reviews,
        'partners' : partners
    }
    return render(request,'Frontpage/about.html',context)

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        description = request.POST.get('description')

        try:
            Enquiry.objects.create(Name=name,Mobile=mobile,Description=description)
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})
    return render(request,'Frontpage/contact.html')

def events(request):
    events = Event.objects.all().order_by('-Date')

    context = {
        'events' : events
    }
    return render(request,'Frontpage/events.html',context)

def gallery(request):
    images = Gallery_Image.objects.all().order_by('-id')

    context = {
        'images' : images
    }
    return render(request,'Frontpage/gallery.html',context)

def packages(request):
    return render(request,'Frontpage/packages.html')

def rides(request):
    return render(request,'Frontpage/rides.html')

@csrf_exempt
def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        description = request.POST.get('description')

        try:
            Review.objects.create(Name=name,Place=place,Description=description)
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})
        
    return render(request,'Frontpage/review.html')