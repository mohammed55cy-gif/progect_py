# Password Strength Checker

## Overview

This is a Python-based password strength checker that evaluates passwords based on several criteria:

- **Entropy Calculation**: Measures the randomness and unpredictability of a password.
- **Dictionary and Pattern Checking**: Utilizes the `zxcvbn` library to detect common patterns, dictionary words, and known weak passwords.
- **Leet Speak Detection**: Identifies common substitutions (e.g., `@` for `a`, `5` for `s`).
- **User-Friendly Recommendations**: Provides actionable tips in English to help users create stronger passwords.

## Features

- Interactive command-line interface.
- Real-time password analysis.
- Detailed report including strength score, entropy, detected patterns, and custom tips.
- Supports graceful exit using `Ctrl+C` or by typing `exit`.

## Installation

1.  **Clone the repository (once uploaded to GitHub):**
    ```bash
    git clone <your-repository-url>
    cd password-strength-checker
    ```

2.  **Install dependencies:**
    This project requires the `zxcvbn` Python library. You can install it using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the password checker, execute the Python script from your terminal:

```bash
python password_checker.py
```

The program will then prompt you to enter passwords for analysis. Type `exit` to quit.

```
Welcome to the Password Strength Checker!
Type 'exit' to quit the program.

Enter a password to check: password123
==================================================
 PASSWORD ANALYSIS REPORT 
==================================================
Password: password123
Strength: Very Weak
Entropy:  56.87 bits
Leet Speak Detected: '1' -> 'i', '3' -> 'e'
Detected Patterns: dictionary

Tips & Recommendations:
  * Add another word or two. Uncommon words are better.
  * - Try to make the password longer (more than 12 characters).
  * - Use a mix of uppercase, lowercase, numbers, and symbols.
  * - Leet speak substitutions are well-known to hackers; don't rely on them alone.
==================================================

Enter a password to check: M@nu5_2026
==================================================
 PASSWORD ANALYSIS REPORT 
==================================================
Password: M@nu5_2026
Strength: Strong
Entropy:  65.7 bits
Leet Speak Detected: '@' -> 'a', '5' -> 's', '0' -> 'o'
Detected Patterns: bruteforce, dictionary

Tips & Recommendations:
  * - Leet speak substitutions are well-known to hackers; don't rely on them alone.
  * - Very good password! Keep using complex passwords.
==================================================

Enter a password to check: exit
Exiting... Stay safe!
```

## Project Structure

- `password_checker.py`: The main Python script containing the password analysis logic.
- `README.md`: This file, providing an overview and instructions.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Any contributions are welcome!
