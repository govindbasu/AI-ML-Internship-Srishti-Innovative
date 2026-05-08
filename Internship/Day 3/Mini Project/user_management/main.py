from auth import register, login, dashboard
from exceptions import UserExistsError, AuthenticationError

def main():
    while True:
        print("\n=== USER MANAGEMENT SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                register()

            elif choice == "2":
                user = login()
                dashboard(user)

            elif choice == "3":
                print("Exiting...")
                break

            else:
                print("Invalid choice!")

        except UserExistsError as e:
            print(e)

        except AuthenticationError as e:
            print(e)

        except Exception as e:
            print("Error:", e)

        finally:
            print("Operation completed.\n")

if __name__ == "__main__":
    main()