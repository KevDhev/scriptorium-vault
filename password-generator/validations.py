def validate_identifier(message: str) -> str:
    #Validates that the identifier contains only alphabetic characters.
    identifier = input(message)

    while not identifier.isalpha():
        print("\nError: You can't enter numbers or symbols for the identifier, only letters.\n")
        identifier = input(message)

    return identifier

def validate_length(message: str) -> int:
    #Ensures the password length is at least 12 characters.
    length = int(input(message))

    while length < 12:
        print('\nError: The minimum length you can enter is 12. \n')
        length = int(input('Enter desired character length (min. 12): '))

    return length

def validate_answers(message: str) -> str:
    #Validates user input to be strictly 'yes' or 'no'.
    response = input(message).lower()

    while not response in ['yes', 'no']:
        print('\nError: You can only answer with “yes” or “no”.\n')
        response = input(message).lower()
    
    return response

def evaluate_security(password: str, punctuation_marks: list[str]) -> str:
    #Evaluates password strength based on character diversity.
    score = 0

    upper_letters = any(character.isupper() for character in password)
    lower_letters = any(character.islower() for character in password)
    digits = any(character.isdigit() for character in password)
    symbols = any(character in punctuation_marks for character in password)

    if upper_letters:
        score += 1
    if lower_letters:
        score += 1
    if digits:
        score += 1
    if symbols:
        score += 1

    if score == 4:
        return 'Very Strong.'
    elif score == 3:
        return 'Strong.'
    elif score == 2:
        return 'Medium.'
    else:
        return 'Weak.'