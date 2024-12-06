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

# The encrypted message
encrypted_message = "gAAAAABnJ6xXV_rlZKvUaNEhrKkzKkY7qqeTUeQnUou1Hy9XjHm94eDw4Kg116N_GC19i0Dwc4sFFKud2P81nQQGXKFx9S7NTHRdJOe5eWRdAb09tzURzNs="

# The key
key = "4pM87rNgte1kHWCMfiJ79eil9JbpCYBvBqRJXec9v-A="

# Create a Fernet object with the provided key
cipher_suite = Fernet(key)

# Decrypt the message
decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()

print(f"Decrypted movie: {decrypted_message}")

