# Name: 
# email: 
# Assignment Number:
# Due Date: 
# Course #/Section:
# Semester/Year:
# Brief Description of the assignment: 
# Brief Description of what this module does: 
# Citations: stack overflow, geeks for geeks
# Anything else that's relevant:

import json
from dataPackage import *

#location py

class findLocation(): 

    def __init__(self, json_file, english_file):
        self.json_file = json_file
        self.english_file = english_file

    def searchTeam(self, teamName):
        # Load the encrypted data from the JSON file
        with open(self.json_file, 'r') as f:
            encrypted_data = json.load(f)
        
        # Look for the team name in the JSON data
        if teamName in encrypted_data:
            return encrypted_data[teamName]
        else:
            print("error finding team name, AdmirableLlama")
    
    def decrypt_location(self, teamName):
        # Search for the team in the encrypted data
        encrypted_location = self.searchTeam(teamName)
        
        # Read the UCEnglish text file into a list of lines
        with open(self.english_file, 'r') as f:
            english_lines = f.readlines()
        
        # Decrypt the location
        decrypted_location = []
        for index in encrypted_location:
            # Convert the index to an integer and use it to get the word from the English file
            word = english_lines[int(index)].strip()  
            decrypted_location.append(word)
        
        # Join the words to form the decrypted statement
        return ' '.join(decrypted_location)

#step 2
#"AdmirableLlama": ["22147", "29029", "28011", "42061", "7480", "27914", "1946", "42061", "23715", "28799", "212"]
