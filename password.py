import random
import string


def generate_password(length):
    # Generate a list of random characters
    characters = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
    # Shuffle the list of characters
    random.shuffle(characters)

    # do a punctionation that we know will not interfere with shell commands.
    characters.append('!')

    # Return the shuffled list of characters as a string
    return ''.join(characters)
