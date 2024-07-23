# Password Strength Checker Tool

![Project Icon](icon.jpg)

This project is a Python-based password strength checker tool that evaluates the strength of a password based on its length, the presence of uppercase and lowercase letters, numbers, and special characters. It provides users with detailed feedback and an overall strength assessment of their password.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [How It Works](#how-it-works)
- [Output Examples](#output-examples)
  - [Password Feedback](#password-feedback)
  - [Password Strength Evaluation](#password-strength-evaluation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Length Check**: Verifies that the password is at least 8 characters long.
- **Case Sensitivity**: Ensures the presence of both uppercase and lowercase letters.
- **Number Check**: Confirms that the password contains at least one digit.
- **Special Characters**: Checks for the inclusion of special characters such as @$!%*?&#.
- **Detailed Feedback**: Provides specific feedback on which criteria are met or not met.
- **Strength Evaluation**: Categorizes the password strength into "very strong," "strong," "medium," or "weak."

## Installation

To use this tool, you need to have Python installed. No additional libraries are required.

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/password-strength-checker.git
    cd password-strength-checker
    ```

2. No additional setup required.

## Usage

1. Run the Python script:

    ```bash
    python password_strength_checker.py
    ```

2. Enter a password when prompted and view the feedback and strength evaluation.

## Example

```bash
$ python password_strength_checker.py
Enter a password to check its strength: ExampleP@ssw0rd!
```

## Feedback:

```bash
Password is very strong.
```

## How It Works

The password strength checker evaluates a password based on several criteria:

    Length: The password must be at least 8 characters long.
    Case Sensitivity: The password should contain both uppercase and lowercase letters.
    Number Check: At least one digit must be present in the password.
    Special Characters: The password should include at least one special character from the set @$!%*?&#.

The tool provides feedback on which criteria are met or missing and evaluates the overall strength based on the number of criteria fulfilled.

## Output Examples
### Password Feedback

#### Original Password

```bash
ExampleP@ssw0rd!
```
#### Feedback:
```bash
Password is very strong.
```
### Password Strength Evaluation

#### Strength Evaluation
```bash
Password is very strong.
```
## Contributing

If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
