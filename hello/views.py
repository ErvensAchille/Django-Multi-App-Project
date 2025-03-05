from django.http import HttpResponse
from django.shortcuts import render

# views.py is the file where you will define the logic for your application. What the user sees.
# The view function is the function that will be called when a user requests a URL from the application.

# Create your views here.

# httpresponse is a function that returns a response to the user.
# Its a special class that needs to be imported from django.http module to return an http response.

# In order to create a view in Django, we're going to define a function. This function, index,
# by convention, takes as argument a request argument. And this is going to be an argument that's going to represent the HTTP request 
# that the user made in order to access our web server. So if we want information about that request, we can look inside of this requested
# object to get access to some other data.
# this function is going to return an HTTP response. And in this case, I'm just going to return a simple string, "Hello, world."
# david and brian are two other views that I've created. 


def index(request):
    return HttpResponse("Hello, world.")

def brian (request):
    return HttpResponse("Hello, Brian.")

def david (request):
    return HttpResponse("Hello, David.")

# create a new function that's just called greet, for example, that also takes a request, 
# but takes an additional parameter. It takes a parameter like someone's name, for example. 
# I can add arbitrary Python logic. It turns out that with any Python string, there is a function or method on that string called 
# capitalize that I can say is just dot capitalize. And if I can do it in Python, then Django allows me to incorporate it into the 
# response that I'm giving back

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")



