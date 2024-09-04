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
        '8': 'B',  # Eight vs. the letter B
        'B': '8',  # The letter B vs. eight
        '6': 'G',  # Six vs. the letter G
        'G': '6',  # The letter G vs. six
        '9': 'g',  # Nine vs. lowercase letter g
        'g': '9',  # Lowercase letter g vs. nine
    }

    suggested_iban = list(iban)

    for i, char in enumerate(iban):
        if char in common_typos:
            # Try replacing typo with possible correct character
            original_char = suggested_iban[i]
            suggested_iban[i] = common_typos[char]

            # Check if the new IBAN is valid
            if is_valid_iban(''.join(suggested_iban)):
                return ''.join(suggested_iban)  # Return valid suggestion

            # Revert change if not valid
            suggested_iban[i] = original_char

    # If no valid IBAN is found, return None
    return None
