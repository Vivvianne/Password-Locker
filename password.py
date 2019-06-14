import string
import random
import pyperclip

#Class variables
#Global variable
global user-list


class User:
    
 '''
 A class to create user accounts and save them
 
 '''
 #global variable user_list
 
 user-list =[]
 
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


