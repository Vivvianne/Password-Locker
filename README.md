# Paswword Locker
Author: Vivvianne Kimani

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts and also generate passwords for their new accounts.

## User story
As a user I would like:

To create an account with my details - log in and password
Store my existing login credentials
Generate a password for a new credential/account
Copy my credentials to the clipboard

## Behavior Driven Development
| Behavior | Input | Ototput |
|:---------|-------|---------|
|In the terminal; Display codes for navigation| The termianl shows;$./password_locker.py| User should see; Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
|The shell should display prompt for creating an account | Enter: ca | Enter your first name, last name and password |
| Display prompt for login in | Enter: li | Enter your account name and password |
| Display codes for navigation | Successful login | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit|
| Display prompt for creating a credential | Enter: cc | Enter the site name, your username and password |
| Display a list of credentials | Enter: dc |Prints a list of saved credentials |
| Display prompt for which credential to copy | Enter: copy | Enter the site name of the credential you wish to copy.|
| Exit application | Enter: ex | Exit the current navigation stage|


## SetUp / Installation Requirements

### Prerequisites

python3.6, 
pip, 
pyperclip, 

## Running the Application
To run the application, in your terminal:

  $ chmod +x run.py
  $ ./run.p

## Technologies Used
Python3.6

## License
MIT
Here is the link to the licence https://github.com/Vivvianne/Password-Locker/pull/1/commits/adb6a11a86421939ebfc760756935a4cb0efc097