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

    
    
    
    