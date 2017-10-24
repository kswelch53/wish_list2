from django.db import models
#for date of hire (doh)
from datetime import date

#This is the model manager class where the logic is done. It needs to go on top.

#This class method handles the user validations. The parament self represents whatever current object of User we're working with. Post_data captures the information we get from request.post. It's sent from the register method in views.py to the validate method below, to be used in the function.

class UserManager(models.Manager):
    def validate_user(self, post_data):
        #creating a dictionary that can return a response to views.py
        response_to_views = {}
        #creating a list to gather up all the errors:
        errors = []
        print("**We are in model method**")
        print(post_data)

        #adding the validations:
        if not len(post_data['name']) > 2:
            errors.append('Name must contain at least 3 characters')

        if not len(post_data['username']) > 2:
            errors.append('Username must contain at least 3 characters')

        if not len(post_data['password']) < 8:
            errors.append('Password must contain at least 8 characters')

        #checking whether form password equals database password
        if not post_data['password'] == post_data['confirm_password']:
            errors.append('Passwords do not match')

        #datetime returns date of hire as a string; this checks that the user-submitted dob is not in the future
        if not post_data['dob'] < str(date.today()):
            print(post_data['dob'])
            errors.append('Date of hire must be in the past')
# GETTING ONLY 1 ERROR MESSAGE AT A TIME

        #Checks for failed validations & builds a dictionary to hold them. Status and errors are dictionary keys; the value of status is either true or false, and the value of errors is whatever error message(s) are appended
        if errors:#validations failed
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:#validations passed
            response_to_views['status'] = True

            #The user can now be created in the model, using self.create. Variable user saves the data it can be sent back to views.py
            user = self.create(name = post_data['name'], username = post_data['username'], password = post_data['password'], doh = post_data['doh'])
            #django will convert dob to a datetime object

            response_to_views['user'] = user

        return response_to_views

#LOGIN NOT WORKING
#login function sends to method in main app's views.py:
    def login_user(self, post_data):
        response_to_views = {}#sets up a dictionary
        #uses email to find user in the database
        user = self.filter(username = post_data['username'])
        response_to_views['status'] = True
        response_to_views['user'] = user
        #user's data is sent to views.py

#___________________________________________________________


# Create your model here.
class User(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    confirm_pw = models.CharField(max_length = 255)
    doh = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

#Connects the model and the model manager:
    objects = UserManager()
