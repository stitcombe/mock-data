import hashlib
import string
import random


# Define a function to de-identify a string
def deidentify_value(value):
    if not isinstance(value, str):
        raise AttributeError("Value must be a string.")

    if not value:
        return value

    # Define a salt value
    salt = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    # Add the salt to the original value
    salted_value = salt + value
    # Hash the salted value using SHA-256
    hashed_value = hashlib.sha256(salted_value.encode()).hexdigest()
    # Convert the hexadecimal representation to a string of numeric characters
    numeric_value = "".join([str(int(c, 16) % 10) for c in hashed_value])[:15]
    # Add the first two characters from the original value to the de-identified value
    deidentified_value = value[:2] + numeric_value[2:]
    return deidentified_value
