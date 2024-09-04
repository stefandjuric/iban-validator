import re

def is_valid_iban(iban):
    # Validate IBAN length and format for Montenegro
    if len(iban) != 22 or not iban.startswith('ME'):
        return False

    # Move the first four characters to the end and replace letters with numbers
    rearranged = iban[4:] + iban[:4]
    numeric_iban = ''.join(str(int(char, 36)) for char in rearranged)
    
    # Validate using mod 97
    return int(numeric_iban) % 97 == 1

def suggest_correct_iban(iban):
    """
    Suggests a correct IBAN based on common mistakes.
    """
    # Common typos with possible replacements
    common_typos = {
        '0': 'O',  # Zero vs. the letter O
        'O': '0',  # The letter O vs. zero
        '1': 'I',  # One vs. the letter I
        'I': '1',  # The letter I vs. one
        '2': 'Z',  # Two vs. the letter Z
        'Z': '2',  # The letter Z vs. two
        '5': 'S',  # Five vs. the letter S
        'S': '5',  # The letter S vs. five
        # Add other common typos if needed
    }

    suggested_iban = list(iban)

    for i, char in enumerate(iban):
        if char in common_typos:
            # Suggest replacing typo with correct character
            suggested_iban[i] = common_typos[char]
            if is_valid_iban(''.join(suggested_iban)):
                print(suggested_iban[i])  # Print the corrected character
                break  # Stop at the first detected mistake for simplicity
            print(''.join(suggested_iban))  # Print the suggested IBAN

    # Recreate the IBAN string
    suggested_iban = ''.join(suggested_iban)

    # Validate if the suggested IBAN is now valid
    if is_valid_iban(suggested_iban):
        return suggested_iban
    else:
        return None  # Return None if no valid suggestion is found
