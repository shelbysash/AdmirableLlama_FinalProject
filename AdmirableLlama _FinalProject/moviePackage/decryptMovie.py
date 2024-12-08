# Name: Shelby Sash, Sidney Huschart, JD Poindexter, Drew Mehlman
# email: sashsk@mail.uc.edu, huschash@mail.uc.edu, poindejd@mail.uc.edu, mehlmadm@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate using Github to Decrypt two specified strings
# Brief Description of what this module does: Decrypts the string in the 'TeamsAnd...ect' text file
# Citations: stack overflow, geeks for geeks, reddit, Python.org
# Anything else that's relevant: N/A

#use 'teams and encrypted' json file
#install cryptography.fernet


from cryptography.fernet import Fernet
class movieDecryption():
    """
    Uses Fernet to decrypt the name of a movie
    """
   
    def __init__(self, encrypted_message, key):
        """
        Initializes instance of movieDecryption class 
        @param self: the instance of the class
        @param encrypted_message: the message to be decrypted
        @param key: the personalized key for our team for the decryption
        @return: None
        """
        self.encrypted_message = encrypted_message
        self.key = key
        self.cipher_suite = Fernet(self.key)

    def decrypt(self):
        """
        Initializes instance of movieDecryption class 
        @param self: the instance of the class
        @return: The final decrypted message, the movie name
        """
        # Decrypt and return message
        return self.cipher_suite.decrypt(self.encrypted_message.encode()).decode()

