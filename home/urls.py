"""eve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home),
    path('children/',views.children,name='student'),
    path('education/',views.education,name='education'),
    path('AnnualReport/',views.annualreport,name='annualreport'),
    path('JoinMission/',views.joinmission,name='joinmission'),
    path('team/',views.team,name='team'),
    path('location/',views.location,name='location'),
    path('copyrightpolicy/',views.copyrightpolicy,name='copyrightpolicy'),
    path('termsofus/',views.termsofus,name='termsofus'),
    
    path('faqs/',views.faqs,name='faqs'),
    path('contactus/',views.contactus,name='contactus'),
    path('careers/',views.careers,name='careers'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('payment/',views.payment,name='payment'),
]
