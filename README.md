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
|----------|--------|--------|
|The shell should display prompt for creating an account | Enter: ca | Enter your first name, last name and password |
|---------|-------|----------|
| Display prompt for login in | Enter: li | Enter your account name and password |
|---------|-------|----------|
| Display codes for navigation | Successful login | 