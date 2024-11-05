import random
import string
import os

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_discord_token():
    characters = string.ascii_letters + string.digits  # Pre-generated set of characters
    token = ''.join(random.choice(characters) for _ in range(24))

    # Add the required prefix and suffix to the token
    return 'MTA3MDM0MTQwMTQxMTM0MjM0Nw.' + token + '.8DzH3RREj_l6lA93FtNf-c6DKyec6blfxXzi_Y'

def token_generator():
    num_tokens = int(input("How many tokens do you want to generate? "))

    tokens = [generate_discord_token() for _ in range(num_tokens)]

    # Print all tokens at once
    print("\n".join(tokens))

    # Ask the user if they want to continue and save the file
    save_file = input("Do you want to save the tokens to a file? (y/n): ").lower()
    if save_file == 'y':
        # Get the file path where the user wants to save the file
        file_path = input("Enter the file path where you want to save the tokens (including the file name) [Leave blank to save to the Downloads folder]: ")

        # If the user left the file path blank, save the file to the Downloads folder
        if file_path == "":
            file_path = os.path.join(os.path.expanduser("~"), "Downloads", "GeneratedTokens.txt")

        # Create a file at the specified path and write the tokens to it
        with open(file_path, 'w') as f:
            f.write("\n".join(tokens) + '\n')

        print('Tokens saved to file at the specified path')

def main():
    while True:
        
        choice = input("Enter your 1 to begin,and to 2 exit : ")

        if choice == '1':
            token_generator()
        elif choice == '2':
            print("Exiting the program...")
            break
        else:
            print("Invalid option! Please select again.")

if __name__ == '__main__':
    main()



