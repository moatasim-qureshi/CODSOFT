import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = " ".join(random.choice(characters)for i in range(length))
    return password
try:
    length = int(input("ENTER LENGTH FOR YOUR PASSWORD: "))
    print()

    if length > 0:
        print("  YOUR PASSWORD:",generate_password(length))
        print()
    
    else:
        print("LENGTH MUST BE NON ZERO AND POSITIVE")

except ValueError:
    print("INVALID KEY")