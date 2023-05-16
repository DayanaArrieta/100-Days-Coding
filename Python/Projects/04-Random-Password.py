import random
import string

def generate_password(length=12):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    # Get the desired length of the password from the user
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Print the password
    print("Your password is: ", password)

if __name__ == '__main__':
    main()
