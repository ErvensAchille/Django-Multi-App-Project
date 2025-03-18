from django.http import HttpResponse
from django.shortcuts import render

# views.py is the file where you will define the logic for your application. What the user sees.
# The view function is the function that will be called when a user requests a URL from the application.

# Create your views here.

# httpresponse is a function that returns a response to the user.
# Its a special class that needs to be imported from django.http module to return an http response.

# In order to create a view in Django, we're going to define a function. This function, index,
# by convention, takes as an argument the request argument. This is going to be an argument that's going to represent the HTTP request 
# that the user made in order to access our web server. So if we want information about that request, we can look inside of this requested
# object to get access to some other data.
# this function is going to return an HTTP response. And in this case, I'm just going to return a simple string, "Hello, world."
# david and brian are two other views that I've created. 


# def index(request):
#     return HttpResponse("Hello, world.")

# I want to render an entire HTML file, I can call this render function, pass in the request, but then also pass
#  in the name of a template. inside of the hello directory, I'll create a new folder called templates.

def index(request):
    return render (request, "hello/index.html")

def brian (request):
    return HttpResponse("Hello, Brian.")

def david (request):
    return HttpResponse("Hello, David.")


# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}")

# # we've generally tried to separate out different parts of our application wherever possible. 
# # And so the way we can do that is, instead of returning an HTTP response, I can instead-- let's say for this default route, instead of 
# # returning an HTTP response of hello, let me go ahead and render. And when I render something I need to pass in the HTTP request. But 
# # I'll also pass in the name of a template. And I'll go ahead and call this template hello/index.html. 
# # So if I don't want to render just a string, but I want to render an entire HTML file, I can call this render function, pass in the
# #  request, but then also pass in the name of a template. And now all I need to do is create that template. So let me go ahead, and inside
# #  of the hello directory, I'll create a new folder called templates. 

def greet (request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

# # create a new function that's just called greet, for example, that also takes a request, 
# # but takes an additional parameter. It takes a parameter of someone's name.
# # I can add arbitrary Python logic. It turns out that with any Python string, there is a function or method on that string called 
# # capitalize that I can say is just dot capitalize. And if I can do it in Python, then Django allows me to incorporate it into the 
# # response that I'm giving back
