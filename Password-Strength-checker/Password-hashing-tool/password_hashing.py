import hashlib
import os
import getpass


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt.hex(), password_hash.hex()


def verify_password(password, salt_hex, stored_hash):
    salt = bytes.fromhex(salt_hex)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return password_hash.hex() == stored_hash


def main():
    print("=" * 50)
    print("        PASSWORD HASHING TOOL")
    print("=" * 50)

    password = getpass.getpass("Enter password: ")

    salt, password_hash = hash_password(password)

    print("\nGenerated Salt:")
    print(salt)

    print("\nPassword Hash:")
    print(password_hash)

    print("\nHashing completed successfully.")


if __name__ == "__main__":
    main()
