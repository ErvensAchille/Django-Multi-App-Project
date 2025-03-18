import datetime
from django.shortcuts import render


# Create your views here. 

# I'll define an index function that takes an HTTP request as an argument. 
# And now inside of this index function, Add some logic that checks whether or not it's January 1. 
# there is a date time module in Python that I can import.
# And I can get the current date and time by calling datetime.datetime.now.
# And now I can return a response that's going to be rendered by Django.
# And I'll pass in the request and then the name of a template.
# And I'll call this template newyear/index.html.
# And now I need to create that template.
# So I'll create a new folder inside of the newyear directory called templates.
# And inside of that folder, I'll create a new file called index.html.
# And inside of that file, I'll just put some simple HTML.
# And I'll say, if it is the new year, I'll say, "Yes, it is the new year."
# Otherwise, I'll say, "No, it is not the new year." And this newyear variable that I'm passing in to my template will be 
# equal to now.month equals 1 and now.day equals 1. So if it is the case that after I get the current date and time by running
#  datetime.datetime.now, saving the result inside of this variable called now, if both and the day are equal to 1, then the value of 
# this new year variable is going to be true when the template gets access to it. Otherwise, as it is the case today and on most days, 
# the value of that variable is going to be false. 






def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {

        'newyear': now.month == 1 and now.day == 1
        
    })
# This is the view function that will be called when a user visits the URL of the application.

