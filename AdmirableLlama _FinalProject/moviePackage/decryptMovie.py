# Name: 
# email: 
# Assignment Number:
# Due Date: 
# Course #/Section:
# Semester/Year:
# Brief Description of the assignment: 
# Brief Description of what this module does: 
# Citations: Microsoft Copilot
# Anything else that's relevant:

#use 'teams and encrypted' json file
#install cryptography.fernet


from cryptography.fernet import Fernet
class movieDecryption():
   
    def __init__(self, encrypted_message, key):
        self.encrypted_message = encrypted_message
        self.key = key
        self.cipher_suite = Fernet(self.key)

    def decrypt(self):
        # Decrypt and return message
        return self.cipher_suite.decrypt(self.encrypted_message.encode()).decode()

