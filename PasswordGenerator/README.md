# Password Generator

## Overview

The **Password Generator** is a Python command-line application that generates strong and random passwords based on user preferences. The user can specify the password length and choose whether to include uppercase letters, lowercase letters, numbers, and special characters. The application uses Python's built-in `secrets` module to ensure secure password generation.

---

## Features

* Generate secure random passwords
* User-defined password length
* Option to include:

  * Uppercase letters (A-Z)
  * Lowercase letters (a-z)
  * Numbers (0-9)
  * Special characters (!, @, #, $, etc.)
* Input validation for password length
* Secure password generation using the `secrets` module
* Simple and user-friendly command-line interface

---

## Project Structure

```text
PasswordGenerator/
│
├── password_generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Prerequisites

* Python 3.8 or higher

No external Python packages are required.

---

## Installation

### 1. Clone the repository (optional)

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd PasswordGenerator
```

---

## Running the Application

Execute the following command:

```bash
python3 password_generator.py
```

---

## Sample Output

```text
==================================================
      Secure Password Generator
==================================================

Enter password length (minimum 4): 16

Choose character types:

Include Uppercase Letters? (y/n): y
Include Lowercase Letters? (y/n): y
Include Numbers? (y/n): y
Include Symbols? (y/n): y

Generated Password:
------------------------------
H#7kP!9x@Lm2Q$wR
------------------------------
```

---

## Technologies Used

* Python 3
* `secrets` (Built-in module)
* `string` (Built-in module)

---

## Learning Outcomes

This project helps you understand:

* Python functions
* User input handling
* Conditional statements
* Loops
* String manipulation
* Secure random password generation
* Modular programming

---

## Future Enhancements

* Password strength meter
* Copy password to clipboard
* Save generated passwords to a file
* Generate multiple passwords at once
* Graphical User Interface (GUI)
* Password history feature

---

## License

This project is developed for educational and learning purposes. Feel free to modify and enhance it according to your requirements.
