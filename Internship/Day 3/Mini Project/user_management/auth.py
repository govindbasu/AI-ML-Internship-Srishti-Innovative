from file_handler import read_users, write_user, update_user, delete_user
from utils import validate_password, encrypt_password
from exceptions import UserExistsError, AuthenticationError
from log import log_action

def register():
    users = read_users()

    username = input("Enter username: ")
    if username in users:
        raise UserExistsError("User already exists!")

    password = input("Enter password: ")
    validate_password(password)

    encrypted = encrypt_password(password)
    write_user(username, encrypted)

    log_action(f"Registered: {username}")
    print("Registration successful!")

def login():
    users = read_users()

    for i in range(3):
        username = input("Username: ")
        password = input("Password: ")

        encrypted = encrypt_password(password)

        if username in users and users[username] == encrypted:
            log_action(f"Login success: {username}")
            print("Login successful!")
            return username
        else:
            print("Invalid credentials!")

    raise AuthenticationError("3 failed attempts!")

def dashboard(username):
    while True:
        print("\n--- Dashboard ---")
        print("1. View Profile")
        print("2. Update Password")
        print("3. Delete Account")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"Welcome, {username}")

        elif choice == "2":
            new_pass = input("Enter new password: ")
            validate_password(new_pass)

            update_user(username, encrypt_password(new_pass))
            log_action(f"Password updated: {username}")
            print("Password updated!")

        elif choice == "3":
            delete_user(username)
            log_action(f"Deleted: {username}")
            print("Account deleted!")
            break

        elif choice == "4":
            log_action(f"Logout: {username}")
            print("Logged out.")
            break

        else:
            print("Invalid choice!")