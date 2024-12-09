# Name: Shelby Sash, Sidney Huschart, JD Poindexter, Drew Mehlman
# email: sashsk@mail.uc.edu, huschash@mail.uc.edu, poindejd@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using Github to decrypt two specified strings
# Brief Description of what this module does: Decrypts the string in the 'EncryptedGroup...ect' text file using the UCEnglish file
# Citations: stack overflow, geeks for geeks, reddit, Python.org
# Anything else that's relevant: N/A

import json
from dataPackage import *

#location py

class findLocation(): 
    """
    Decrypts a string to return a given location for our teams name
    """

    def __init__(self, jsonFile, UCEnglishFile):
        """
        Initializes instance of findLocation class 
        @param self: the instance of the class
        @param jsonFile: the path to the json file
        @param UCEnglishFile: path to the reference text file
        @return: None
        """
        self.json_file = jsonFile
        self.english_file = UCEnglishFile

    def searchTeam(self, teamName):
        """
        Searches for team 'AdmirableLlama' to find designated encrypted message
        @param self: the instance of the class
        @param teamName: Our team's name to search for
        @return: The encrypted string or None if team not found
        """
        #load the encrypted data from JSON file
        with open(self.json_file, 'r') as f:
            encrypted_data = json.load(f)
        
        # Look for team name in JSON data
        if teamName in encrypted_data:
            return encrypted_data[teamName]
        else:
            print("error finding team name, AdmirableLlama")
    
    def decrypt_location(self, teamName):
        """
        Decrypts the message using the UCEnglish text file
        @param self: the instance of the class
        @param teamName: Our team's name to search for
        @return: The final decrypted string
        """
        #search for team in encrypted data
        encrypted_location = self.searchTeam(teamName)
        
        #read the UCEnglish text file into a list of lines
        with open(self.english_file, 'r') as f:
            english_lines = f.readlines()
        
        #decrypt the location
        decrypted_location = []
        for index in encrypted_location:
            # Convert the index to an integer and use it to get the word from the English file
            word = english_lines[int(index)].strip()  
            decrypted_location.append(word)
        
        #form the decrypted statement
        return ' '.join(decrypted_location)

#step 2
#"AdmirableLlama": ["22147", "29029", "28011", "42061", "7480", "27914", "1946", "42061", "23715", "28799", "212"]
