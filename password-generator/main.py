import string
from secrets import choice
from pyperclip import copy
from validations import *
from file_management import *

# Character sets for password generation
UPPER_LETTERS = string.ascii_uppercase
LOWER_LETTERS = string.ascii_lowercase
DIGITS = string.digits
PUNCTUATION_MARKS = string.punctuation
FILE_NAME = 'passwords.txt'     # Output file name
possible_characters = []

print('====================================')
print('Secure Password Generator | KevDhev')
print('==================================== \n')

file_exists(FILE_NAME)

# Main loop: generates password until at least one character set is selected.
while not possible_characters:
    identifier = validate_identifier('Enter an identifier for the password (email, instagram, etc.): ')
    
    length = validate_length('Enter desired character length (min. 12): ')

    print('\nYou must answer “yes” to at least one of the following options:\n')

    upper_case = validate_answers('Do you want to include capital letters? (yes/no): ')
    lower_case = validate_answers('Do you want to include lowercase letters? (yes/no): ')
    numbers = validate_answers('Do you want to include numbers? (yes/no): ')
    symbols = validate_answers('Do you want to include symbols? (yes/no): ')

    if upper_case == 'yes': possible_characters.extend(UPPER_LETTERS)
    if lower_case == 'yes': possible_characters.extend(LOWER_LETTERS)
    if numbers == 'yes': possible_characters.extend(DIGITS)
    if symbols == 'yes': possible_characters.extend(PUNCTUATION_MARKS)

password = ''.join(choice(possible_characters) for _ in range(length))

copy(password)

print(f'\nCongratulations, your new password is: {password}')
print(f'The security level of your password is: {evaluate_security(password, PUNCTUATION_MARKS)}')

save_password(FILE_NAME, password, identifier)

print('\nThe password has been copied to the clipboard and saved in the file “passwords.txt”.\n')