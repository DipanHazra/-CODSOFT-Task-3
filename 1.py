import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        char = string.ascii_letters
    elif complexity == "medium":
        char = string.ascii_letters + string.digits
    elif complexity == "hard":
        char = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity ,Try again ")

    password = ''.join(random.choice(char) for i in range(length))
    return password

def main():
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter the complexity level: easy or medium or hard :\n")

        password = generate_password(length, complexity)
        print("Generated Password:", password)


if __name__ == "__main__":
    main()
