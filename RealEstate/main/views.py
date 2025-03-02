from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

# Home Page
def home_view(request:HttpRequest):
  return render(request, "main/index.html")

# properties 
def properties_view(request:HttpRequest):
  properties = [
    {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
    {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
    {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
    {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
]
  return render(request, "main/properties.html", context={"properties":properties})

# contact_view 
def contact_view(request:HttpRequest):
  return render(request, "main/contact.html")