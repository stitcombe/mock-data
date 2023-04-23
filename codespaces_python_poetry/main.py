import json
import hashlib

# Load the JSON file
with open('claim_mock.json', 'r') as f:
    data = json.load(f)

# Define a function to de-identify a string
def deidentify_string(s):
    # Use SHA-256 hash function to generate a new, de-identified value
    hash_value = hashlib.sha256(s.encode()).hexdigest()
    # Retain the first 2 characters of the original value within the de-identified value
    deidentified_value = s[:2] + hash_value
    # Truncate the de-identified value to a maximum of 15 characters
    return deidentified_value[:15]

# Loop through each item in the JSON data
for item in data:
    # Check if the 'claim' key is present in the item
    if 'claim' in item:
        claim = item['claim']
        # Check if the 'claimNumber' key is present in the claim dictionary
        if 'claimNumber' in claim:
            # De-identify the value of the 'claimNumber' key
            claim['claimNumber'] = deidentify_string(claim['claimNumber'])
        # Check if the 'memberId' key is present in the claim dictionary
        if 'memberId' in claim:
            # De-identify the value of the 'memberId' key
            claim['memberId'] = deidentify_string(claim['memberId'])

# Write the updated JSON data to a file
with open('your_updated_file.json', 'w') as f:
    json.dump(data, f)
