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
        # Check if the 'familyId' key is present in the claim dictionary
        if "familyId" in claim:
            # De-identify the value of the 'familyId' key
            claim["familyId"] = function.deid_memberId(claim["familyId"])
        # Check if the 'firstName' key is present in the claim dictionary
        if "firstName" in claim:
            # De-identify the value of the 'firstName' key
            claim["firstName"] = function.deid_memberName(claim["firstName"])
        # Check if the 'lastName' key is present in the claim dictionary
        if "lastName" in claim:
            # De-identify the value of the 'firstName' key
            claim["lastName"] = function.deid_memberName(claim["lastName"])
        # Check if the 'memberBirthdate' key is present in the claim dictionary
        if "memberBirthdate" in claim:
            # De-identify the value of the 'memberBirthdate' key
            claim["memberBirthdate"] = function.deid_memberDob(claim["memberBirthdate"])
        # Check if the 'memberAge' key is present in the claim dictionary
        if "memberAge" in claim:
            # De-identify the value of the 'memberAge' key
            claim["memberAge"] = function.deid_memberAge(claim["memberAge"])
        # Check if the 'PAMCNBR' key is present in the claim dictionary
        if "PAMCNBR" in claim:
            # De-identify the value of the 'PAMCNBR' key
            claim["PAMCNBR"] = function.deid_prior_auth(claim["PAMCNBR"])
        # Check if the 'PRAuthNbr' key is present in the claim dictionary
        if "PRAuthNbr" in claim:
            # De-identify the value of the 'PAMCNBR' key
            claim["PRAuthNbr"] = function.deid_prior_auth(claim["PRAuthNbr"])
        # Check if the 'Message' key is present in the claim dictionary
        if "Message" in claim:
            # De-identify the value of the 'Message' key
            claim["Message"] = function.deid_message(claim["Message"])
        # Check if the 'Message' key is present in the claim dictionary
        if "Message2" in claim:
            # De-identify the value of the 'Message' key
            claim["Message2"] = function.deid_message(claim["Message2"])
        # Check if the 'Message' key is present in the claim dictionary
        if "Message3" in claim:
            # De-identify the value of the 'Message' key
            claim["Message3"] = function.deid_message(claim["Message3"])
        # Check if the 'DUR' key is present in the claim dictionary
        if "DUR" in claim:
            # De-identify the value of the 'DURConflictingClaim' key in each DUR item
            for dur in claim["DUR"]:
                if "DURConflictingClaim" in dur:
                    dur["DURConflictingClaim"] = function.deid_claim(
                        dur["DURConflictingClaim"]
                    )


# Write the updated JSON data to a file
with open(outputFile, "w") as f:
    json.dump(data, f)
