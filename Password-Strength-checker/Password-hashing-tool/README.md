# Password Hashing Tool

A beginner-friendly Python cybersecurity tool that securely hashes passwords and verifies them using PBKDF2 with SHA-256.

## Features

- Secure password hashing
- PBKDF2 key derivation
- SHA-256 hashing algorithm
- Random salt generation
- Password verification
- Command-line interface

## Technologies Used

- Python
- hashlib
- secrets
- PBKDF2
- SHA-256

## How It Works

1. The user enters a password.
2. A random salt is generated.
3. PBKDF2 derives a secure hash using SHA-256.
4. The password hash and salt are stored/returned.
5. A password can later be verified against the stored hash.

## Usage

Run the program with:

```bash
python password_hashing.py
