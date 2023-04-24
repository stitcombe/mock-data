import json
import function
from pathlib import Path

filepath = Path(__file__).parent / "claim_mock.json"

# Load the JSON file
with open(filepath, "r") as f:
    data = json.load(f)

# Loop through each item in the JSON data
for item in data:
    # Check if the 'claim' key is present in the item
    if "claim" in item:
        claim = item["claim"]
        # Check if the 'claimNumber' key is present in the claim dictionary
        if "claimNumber" in claim:
            # De-identify the value of the 'claimNumber' key
            claim["claimNumber"] = function.deidentify_value(claim["claimNumber"])
        # Check if the 'memberId' key is present in the claim dictionary
        if "memberId" in claim:
            # De-identify the value of the 'memberId' key
            claim["memberId"] = function.deidentify_value(claim["memberId"])

# Write the updated JSON data to a file
with open("your_updated_file.json", "w") as f:
    json.dump(data, f)
