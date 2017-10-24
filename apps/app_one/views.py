from django.shortcuts import render, HttpResponse, redirect
#This connects the model to the methods:
from .models import User

#this allows flashed messages:
from django.contrib import messages

# Create your views here.
def index(request):
    print("I am index function in views.py")
    return render(request, 'app_one/index.html')

#When users hit the submit button, the app-level urls.py's named "register" route routes to views.py's register method, which picks up the form info, calls the model method validate_user and sends it to models.py for validation:
def register(request):#handles registering a user
    if request.method == "POST":
        print("**This is request method in views.py**")
        print(request.POST)

        #With model imported, you can use the method from the model manager to validate data.
        #this will capture the result of response_to_views; storing the data we get from the validate_user method:
        response_from_models = User.objects.validate_user(request.POST)
        print(response_from_models)
        #use validations go here, get info from the form to use in validate_user method created in the manager

        #Sending user to the success page after successful login or registering:
        if response_from_models['status']:
            #if status = true, passed validations and created a new user
            #saving the user id
            #You can identify the user, put name or other info on the page
            request.session['user_id'] = response_from_models['user'].id
            #sends user to the success page via the second app (wishlist route in main urls.py)
            return redirect('wishlist:index')#switches to 2nd app, index method
        else:
            #adds flash messages to the html, loops through r_f_m dictionary
            for error in response_from_models['errors']:
                messages.error(request, error)#sends request for whichever error
                return redirect('users:index')#error messages go on users route (1st app), index method (index.html)

    else:
        #uses the named routes to redirect to the index method
        #prevents users from getting to the register page directly; they have put their info in and hit the register button
        return redirect('users:index')


#login method goes here NONETYPE OBJECT NOT SUBSCRIPTABLE
# has a model method in models.py's UserManager
def login(request):
    response_from_models = User.objects.login_user(request.POST)
    print(response_from_models)
    #models.py checks user's email/password with the database and returns true or false
    if response_from_models['status']:
        #successful login stores user id in session:
        request.session['user_id'] = response_from_models['user'].id
    else:#unsuccessful attempt returns an error message and redirects to start page
        messages.error(request, response_from_models['errors'])
        return redirect('users:index')


#logout method goes here
#this logs the user out by deleting everything in session
def logout(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('users:index')
