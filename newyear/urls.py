from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name ='index'),
]

# Now, that file isn't given to us by default, so we need to create it. I need to go into my newyear folder 
# and create a new file called urls.py. And inside of that file, I'll do from django.urls import path, from . 
# import views, and then define some urlpattern, same as before, where I'll just have a single path that loads the index 
# function inside of views.py. And it has a name of index. this app is just going to have a single route, the empty route, 
# that loads the index function. 