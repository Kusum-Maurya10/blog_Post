from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse('This is home')

def about(request):
    return render(request, 'home/about.html')
    #return HttpResponse('This is about')

def contact(request):
    return render(request, 'home/contact.html')
    #return HttpResponse('This is contact')
