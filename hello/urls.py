from django.urls import path
from . import views

# urls.py needs to define a variable called urlpatterns, which will be a list of all of the allowable URLs that can be accessed for 
# this particular app. 

urlpatterns = [
    path('', views.index, name ='index'),
    path('brian', views.brian, name ='brian'),
    path('david', views.david, name ='david'),
    path('<str:name>', views.greet, name ='greet')
# the url, the view function, and the name of the url
]

# So I'll go ahead and go into the hello directory. And I'll create a new file inside of the hello directory called you urls.py. And what urls.py needs is, it needs to define a variable called urlpatterns, which will be a list of all of the allowable URLs that can be accessed for this particular app. 

# And the way you create a URL is by first importing from django.urls import path. And let's create our first URL. I'll say path. And then the first argument here, I'm going to give the empty string to mean no additional argument-- and we'll see what that means in just a moment-- meaning nothing at the end of the route. 

# And then the second argument to path is what view should be rendered when this URL is visited. And so if I want to render my index view-- recall that in views.py over here, I have this index function-- then what I want to render when someone visits this URL, the empty URL, is going to be views.index. Views represents views.py, that file where I've defined all of my views. And an index just so happens to be the name of the function that I want to call when someone visits this URL, for example. 

# And then you can optionally provide a path with a string name . To represent this URL I'm going to give this a name of index. We'll see why this can be useful later on, but the idea is, giving a name to a particular URL pattern makes it easy to reference it from other parts of the application. So later when we might want to link to things or have forms that are submitting to different parts of the web application, giving a name to a path can be a useful tool. 

# In order to use views, last line I need to add to urls.py is to say from dot, in other words, from the current directory, go ahead and import views. Anytime I'm using a variable name like views, I'm using that name, I need to import it from somewhere. And it just so happens that views.py and urls.py are located in the same directory. So I can just say from dot import views to import all of that into this particular file. 

