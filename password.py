import string
import random
import pyperclip

#Class variables
#Global variable

global user_list


class User:
    
 '''
 A class to create user accounts and save them
 
 '''
 #global variable user_list
 
 user_list =[] #empty user list
 
 def __init__(self, firstname, lastname, password):
    '''
    method to define what property will be in each user object
    '''
    #intance variables
    self.first_name = first-name
    self.last_name = last_name
    self.password = password

def save_user(self):
    '''
    function to save new user instances created
    '''
    User.user_list.apend(self)


class Creditial:
    '''
    Class to create account credentials, generate passwords 
    and save their information.
    '''
    
   #Class variables
   credetials_list = []
   user_credentials_list = []
   
   @classmethod
   def check_user(cls,firstname,password):
       '''
       Method that checks the name and password entered match the ones in the users_list.
       
       '''
       current user = ''
       
       for user in User.user_list:
           if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user
    
    