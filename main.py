# Django is a web framework. 
# It's a set of tools that is already built for us that's just going to make it easy to get started by writing Python code in
# order to design a fully fledged web application by taking care of some of the stuff that most web pages all have to do such that we 
# can focus on the interesting logic of building our own web applications.

# Django comes preloaded with its ability to take a project and divide it into multiple distinct apps. Maybe for simpler apps, 
# we're only going to have a project that has one app inside of it instead of multiple. But it has the ability to allow us to create 
# these separate apps that have different capacities. 

# in the terminal, we can run a command to be able to create a Django project. And that command looks something like this,

# pip is the Python package manager to install new packages. 
# And the first thing we'll probably want to do is install Django. Using Python 3, 
# you might need to specify "pip3 install Django" to install Django on your system.

# what we're going to be trying to create using this Django web framework. 
# We're going to be creating software that's going to run on a web server such that clients, running in their web browser, 
# can make requests to our web server. And our server is going to respond back with some sort of response. 

# So how does this process actually happen? Well ultimately, it boils down to this protocol, HTTP, otherwise known as the HyperText 
# Transfer Protocol, which is the protocol for how messages are going to be sent back and forth over the internet. 
# In this case, you can think about this as a computer, some user, which we might call the client, and then our server, 
# which is going to be the server that is going to contain our web application. 

# We can run a command to be able to create a Django project. And that command looks something like this, django-admin startproject 
# followed by the name of the project that we would like to create. ex :
# 
#  django-admin startproject myproject
# 
# When we run this command, Django is automatically going to create some starter files for us just to get started with the process of 
# building a web application. i.e. urls.py, settings.py, urls.py, views.py etc in a directory called myproject.

# But first and foremost, manage.py is a file that Django is going to create for us. We'll generally not need to touch that file,
#  but we're going to use the manage.py file to be able to execute commands on this Django project. And we'll see a couple of examples of 
# that now and a couple of examples of that in future lectures as well. 

# And then the other important one that we'll be looking at is settings.py, which just contains important configuration settings 
# for our Django application. Settings.py comes preloaded with a couple of default settings, but we might want to change those settings
#  to be able to add features to our application as well or make some modifications to how the application behaves. 

# And then the other important file that's pre-created for us now here is urls.py. And you can think of urls.py as a sort of table 
# of contents for our web application, that on any given web application, on a website, there are a number of different URLs or routes 
# that you can visit. On Google, for example, you can visit /search or /images. And urls.py is just going to be a table of contents of 
# all of URLs on my web application that I can ultimately visit. 

# And so if I'd like to try running this web application just to see what it looks like, the way to do it in Django is, 
# in the terminal, I'll run python manage.py followed by a command. And the command is called runserver. And so this is 
# generally how we'll use manage.py. We'll manage.py followed by an argument specifying what command we would like to run. 
# And python manage.py runserver means go ahead and actually run this web server. 

# And if I do this, I'm now running this web server locally.
#  And I see a bunch of debugging output. But the interesting point to me is that it says down here, 
# starting development server at http://127.0.0.1:8000 And so this is where my web application is currently running, 127.0.0.1 
# is an IP address, an address on the internet that just refers to my local computer, the computer I'm looking at right now. 
# So only I can access this, not anyone else on the internet. 

# 1) 
# In terminal run the command python manage.py startapp and then the name of the app
# ex: python manage.py startapp hello

# 2) 
# if I want to add my new app that I've just created called hello to these installed apps, I'll go ahead and just add to this list of strings, this INSTALLED_APPS variable, 
# I'll just add hello. And so now hello is going to be an installed app on this particular Django project. 

#     'hello.apps.HelloConfig', # This is the app we created and added to the list of installed apps

# 3)  views.py is the file where you will define the logic for your application. What the user sees. 
# create views for users. # In order to create a view in Django, we're going to define a function. So this function I'll just call index. This function, 
# by convention, takes as argument a request argument. And this is going to be an argument that's going to represent the HTTP request 
# that the user made in order to access our web server. So if we want information about that request, we can look inside of this requested
# object to get access to some other data. In order to create a view in Django, we're going to define a function. So this function I'll just call index. 
# This function, by convention, takes as argument a request argument. And this is going to be an argument that's going to represent the 
# HTTP request that the user made in order to access our web server. So if we want information about that request, we can look inside of 
# this requested object to get access to some other data.

# def index(request):
#     return HttpResponse("Hello, world.")


# New Year App:

# So I will now go ahead and create a new app. And I'll call the app newyear. And I can do that by some 
# writing python manage.py startapp new year.  If I type ls,  you'll see that not only do I have a hello directory that 
# represents the hello app, I now have this newyear directory that represents the fact that this is a new app called newyear. 

# As with before, I'll need to go into settings.py inside of my project directory and add newyear as an installed app. 
# This is now a new app that exists in my web application, so it too now needs to be a new installed app. I need to go into urls.py for 
# myproject. And just as before, I had a path saying when I go to /hello, then you should go to all the URLs for the hello app, let me
# add a new path that says that if I go to my application /newyear, well then you should go to all of URLs for the newyear file, go 
# to newyear.urls, representing the urls.py file inside of the newyear app. 
