import hashlib
import string
import random

# Define salt value
salt = "".join(random.choices(string.ascii_letters + string.digits, k=5))
print("The salt value used is: " + salt)


# Define a function to de-identify a claim number
def deid_claim(value):
    if not isinstance(value, str):
        raise AttributeError("Value must be a string.")
    if not value:
        return value
    # Add the salt to the original value
    salted_value = salt + value
    # Hash the salted value using SHA-256
    hashed_value = hashlib.sha256(salted_value.encode()).hexdigest()
    # Convert the hexadecimal representation to a string of numeric characters
    # Truncate at 15 characters
    numeric_value = "".join([str(int(c, 16) % 10) for c in hashed_value])[:15]
    # Add the first two characters from the original value to the de-identified value
    deidentified_value = value[:2] + numeric_value[2:]
    return deidentified_value


# Define a function to de-identify a member id
def deid_memberId(value):
    if not isinstance(value, str):
        raise AttributeError("Value must be a string.")
    if not value:
        return value
    # Add the salt to the original value
    salted_value = salt + value
    # Hash the salted value using SHA-256
    hashed_value = hashlib.sha256(salted_value.encode()).hexdigest()
    # Add the last 3 characters from the original value
    # to first n characters of the hashed value,
    # where n is the length of the input value
    deidentified_value = hashed_value[: len(value) - 3] + value[-3:]
    return deidentified_value


# Define a function to de-identify a member first or last name
def deid_memberName(value):
    if not isinstance(value, str):
        raise AttributeError("Value must be a string.")
    if not value:
        return value
    # Add the salt to the original value
    salted_value = salt + value
    # Hash the salted value using SHA-256
    hashed_value = hashlib.sha256(salted_value.encode()).hexdigest()
    # Convert the hashed value to alpha characters only
    deidentified_value = "".join(filter(str.isalpha, hashed_value))
    # Extract the first n characters of the hashed value,
    # where n is the length of the input value
    deidentified_value = deidentified_value[: len(value)]
    return deidentified_value


# Define a function to de-identify a member age
def deid_memberAge(value):
    if not isinstance(value, int):
        raise AttributeError("Value must be a integer.")
    if not value:
        return value
    # Return a zero value
    return 0
