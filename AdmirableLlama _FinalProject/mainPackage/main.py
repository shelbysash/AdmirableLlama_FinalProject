# Name: Shelby Sash, Sidney Huschart, JD Poindexter, Drew Mehlman
# email: 
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 
# Brief Description of what this module does: 
# Citations: stack overflow, geeks for geeks
# Anything else that's relevant:

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
    # Encrypted message and key
    encrypted_message = "gAAAAABnJ6xXV_rlZKvUaNEhrKkzKkY7qqeTUeQnUou1Hy9XjHm94eDw4Kg116N_GC19i0Dwc4sFFKud2P81nQQGXKFx9S7NTHRdJOe5eWRdAb09tzURzNs="
    key = "4pM87rNgte1kHWCMfiJ79eil9JbpCYBvBqRJXec9v-A="

    # Instantiate MovieDecryption
    decryption = movieDecryption(encrypted_message, key)
   
    # Decrypt and print the message
    print(f"Decrypted Movie: {decryption.decrypt()}")
    
    


if __name__ == "__main__":
    main()

#IMAGE
#to fix error about truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_path = "dataPackage/AdmirableLlama_image.jpeg"

#displaying the image & rotating it
img = Image.open(image_path)
img = img.rotate(180, expand=True)
img.show()



