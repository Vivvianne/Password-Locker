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
    
    def __init__(self, user_name, site_name, account_name, password):
        
        '''
        Method that define properties that each user object will hold.
        
        '''
        #intance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    
    def save_credentials(self):
        '''
        Function to save newly created user instance
        '''
        #global user_list
        
        Credential.credentials_list.append(self)
        @classmethod
        def generate_password(size=9, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
            
            '''
            Function to create 9 character password
            '''
            gen_pass = ''.join(random.choice(char) for_ in range(size) )
            return gen_pass
            
            
            
    @classmethod
    def display_credentials(cls, user_name):
        '''
        Class method to dispaly the list of the credentials saved
        
        '''
        user_credential_list = []
        for credentials in cls.credential_list:
            if credentials.user_name = user_name:
                user_credentials_list.append(credential)
            return user_credentials_list
            
            
            
            
    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        A method that matches the site name and the credentials entered
        '''
        for credential in cls.credential_list:
            if credentials.site_name = site_name:
                return credential
            
            
            
            
    @classmethod
    def copy_credential(cls, site_name):
        '''
        A class method that copys the credentials info after the site name is entered.
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
        
        
        
        
    
        
    
    
    
    
        


        
    

    
    