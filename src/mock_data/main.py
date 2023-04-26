import json
import function
from root_dir import ROOT_DIR

# Define `files` folder  path
files_dir = ROOT_DIR / "files"
inputFile = files_dir / "claim_mock.json"
outputFile = files_dir / "output.json"

# Load the JSON file
with open(inputFile, "r") as f:
    data = json.load(f)

# Loop through each item in the JSON data
for item in data:
    # Check if the 'claim' key is present in the item
    if "claim" in item:
        claim = item["claim"]
        # Check if the 'claimNumber' key is present in the claim dictionary
        if "claimNumber" in claim:
            # De-identify the value of the 'claimNumber' key
            claim["claimNumber"] = function.deid_claim(claim["claimNumber"])
        # Check if the 'memberId' key is present in the claim dictionary
        if "memberId" in claim:
            # De-identify the value of the 'memberId' key
            claim["memberId"] = function.deid_memberId(claim["memberId"])
        # Check if the 'firstName' key is present in the claim dictionary
        if "firstName" in claim:
            # De-identify the value of the 'firstName' key
            claim["firstName"] = function.deid_memberName(claim["firstName"])
        # Check if the 'lastName' key is present in the claim dictionary
        if "lastName" in claim:
            # De-identify the value of the 'firstName' key
            claim["lastName"] = function.deid_memberName(claim["lastName"])

# Write the updated JSON data to a file
with open(outputFile, "w") as f:
    json.dump(data, f)
