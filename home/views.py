from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')




def children(request):
    return render(request,'home/children.html')


def education(request):
    return render(request,'home/education.html')

def annualreport(request):
    return render(request,'home/annualreport.html')

def joinmission(request):
    return render(request,'home/joinmission.html')

def team(request):
    return render(request,'home/team.html')

def location(request):
    return render(request,'home/location.html')

def copyrightpolicy(request):
    return render(request,'home/copyrightpolicy.html')

def termsofus(request):
    return render(request,'home/termsofus.html')



def faqs(request):
    return render(request,'home/faqs.html')


def contactus(request):
    return render(request,'home/contactus.html')


def careers(request):
    return render(request,'home/careers.html')


def aboutus(request):
    return render(request,'home/aboutus.html')

def payment(request):
    return render(request,'home/payment.html')

 




