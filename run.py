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
    
    
def verify_user(first_name, password):
    '''
    Function that verifies the user before generating the credential
    
    '''
    checking_user = Credential.check_user(first_name,password)
    return checking_user
    
    
def generate_password():
    '''
    Function to automatically generate password
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credential(user_name, site_name, account_name, password):
    '''
    Function to create new credential
    '''
    new_credential = Credential(user_name,site_name,account_name,password)
    return new_credential

    


