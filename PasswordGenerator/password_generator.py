import string
import secrets


def generate_password(length, use_upper, use_lower,
                      use_numbers, use_symbols):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():

    print("=" * 50)
    print("      Secure Password Generator")
    print("=" * 50)

    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print("\nChoose character types:")

    upper = input("Include Uppercase Letters? (y/n): ").lower() == "y"
    lower = input("Include Lowercase Letters? (y/n): ").lower() == "y"
    numbers = input("Include Numbers? (y/n): ").lower() == "y"
    symbols = input("Include Symbols? (y/n): ").lower() == "y"

    password = generate_password(
        length,
        upper,
        lower,
        numbers,
        symbols
    )

    if password is None:
        print("\nError: At least one character type must be selected.")
    else:
        print("\nGenerated Password:")
        print("-" * 30)
        print(password)
        print("-" * 30)


if __name__ == "__main__":
    main()