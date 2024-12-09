# Name: Shelby Sash, Sidney Huschart, JD Poindexter, Drew Mehlman
# email: sashsk@mail.uc.edu, huschash@mail.uc.edu, poindejd@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using Github to Decrypt two specified strings
# Brief Description of what this module does: Entry point of the project. Displays the final output. 
# Citations: stack overflow, geeks for geeks, reddit, Python.org
# Anything else that's relevant: N/A

from locationPackage.decryptLocation import *
from dataPackage import *
from moviePackage.decryptMovie import *
from PIL import Image, ImageFile

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
   
#MOVIE DECRYPTION
     
    
#IMAGE
    #to fix error about truncated images
    ImageFile.LOAD_TRUNCATED_IMAGES = True

    image_path = "dataPackage/AdmirableLlama_image.jpeg"

    #displaying the image & rotating it
    img = Image.open(image_path)
    img = img.rotate(180, expand=True)
    img.show()
    

if __name__ == "__main__":
    main()





