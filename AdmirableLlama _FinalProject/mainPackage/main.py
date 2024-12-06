# Name: Shelby Sash, Sidney Huschart, JD Poindexter, Drew Mehlman
# email: 
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 
# Brief Description of what this module does: 
# Citations: 
# Anything else that's relevant:

from locationPackage.decryptLocation import *
from dataPackage import *
from moviePackage.decryptMovie import *

def main():
    #DECRYPTING LOCATION
    # File paths for the JSON and English text files
    json_file = 'dataPackage/EncryptedGroupHints Fall 2024 Section 001.json'  # Path to your encrypted JSON file
    english_file = 'dataPackage/UCEnglish.txt'  # Path to your UCEnglish.txt file
   
    # Instantiate the FindLocation class
    location_finder = findLocation(json_file, english_file)
   
    projectTeam = "AdmirableLlama"
    # Decrypt the location
    location = location_finder.decrypt_location(projectTeam)
   
    # Print the decrypted location
    print(f'Decrypted Location: {location}')
   
    #DECRYPTING MOVIE QUOTE
    movie_json_file = 'dataPackage/TeamsAndEncryptedMessagesForDistribution.json'
    #instantiate movieDecryption class
    movie_decryption = movieDecryption(movie_json_file)
    projectTeamName = "AdmirableLlama"
    #decrypt movie name 
    movieTitle = 
   

if __name__ == "__main__":
    main()