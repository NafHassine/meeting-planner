from django.shortcuts import render

# Create your views here.
def home_view(request):
    context={'meetings' : meeting.objects.count()}
    return render(request,"website/home.html", context=context)
def about_view(request):
    return render(request,"website/about.html")