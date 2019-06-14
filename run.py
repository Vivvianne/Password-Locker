#! /usr/bin/env python3.5

import pyperclip
from password import User



def create_user(fname, lastname, password):
    '''
    Function to create new user account
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    Function to save new user
    '''
    User.save_user(user)
    

