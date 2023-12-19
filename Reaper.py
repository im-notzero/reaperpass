import random

# ASCII art for the Reaper Dictionary interface
ascii_art = """


 ██▀███  ▓█████ ▄▄▄       ██▓███  ▓█████  ██▀███  
▓██ ▒ ██▒▓█   ▀▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
  ░░   ░    ░    ░   ▒   ░░          ░     ░░   ░ 
   ░        ░  ░     ░  ░            ░  ░   ░     
            Created by i'm not zero                                        
"""

# Function to generate a password based on user input words
def generate_password():
    words = []
    print("Please enter three words to generate your password:")
    for i in range(3):
        word = input(f"Enter word {i + 1}: ")
        words.append(word)

    # Construct the password by combining the entered words
    password = ''.join(words)
    return password

# Display ASCII interface
print(ascii_art)
print("Welcome to the Reaper Dictionary!")
print("Generate your password by entering three words.")
print("------------------------------------------------")

# Generate a password
generated_password = generate_password()
print("Your generated password is:", generated_password)