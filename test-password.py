import unittest
import pyperclip
from password import User


class TestUser(unittest.TestCase):
    '''
    Test class that define the test cases for user class behavior
    Arg:
    unittest.TestCase: helps in creating test cases.
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Viv','Kimani', 'her1234')
        
    def test__init__(self):
        '''
        Test to check if the creation of user instances is done properly
        '''
        self.assertEqual(self.new_user.first_name, 'Viv')
        self.assertEqual(self.new_user.last_name, 'Kimani')
        self.assertEqual(self.new_user.password, 'her1234')
        
    def test_save_user(self):
        '''
        Check if the new user info are saved ino the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
    
    
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases of the behaviors for the credential class.
    Args:
        unittest.TestCases: helps in creating test cases.
    '''
    
    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected.
        '''
        self.new_user = User('Viv','Kimani','her1234')
        self.new_user.save_user()
        user1 = User('Viv','Kimani','her1234')
        user1.save_user()
        
        for user in User.users_list:
            if user.first_name = user1.first_name and user.password = user1.password:
                current_user = user.first_name
        return current_user
    
        self.assertEqual(current_user, Credential.check_user(user1.password,user1.first_name))
    
    
    
    