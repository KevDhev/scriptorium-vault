from os import path

initial_structure = """=====================
Generated passwords:
=====================
"""

def file_exists(file_name: str):
    #Creates the password file with initial structure if it doesn't exist.
    if not path.exists(file_name):
        with open(file_name, 'w') as archive:
            archive.write(initial_structure)

def save_password(file_name: str, password: str, identifier: str):
    #Appends a new password with its identifier to the file.
    with open(file_name, 'a') as archive:
        archive.write(f'\n{identifier}: {password}')