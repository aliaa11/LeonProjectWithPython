from user import User
from loan_account import LoanAccount

def main_menu():
    while True:
        print("\n=== Loan Application System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user = User(username, password)
            if user.login():
                user_menu(user)
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = User(username, password)
            user.register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def user_menu(user):
    account = LoanAccount(user.id)
    while True:
        print(f"\nWelcome {user.username}")
        print("1. Apply for loan")
        print("2. Make payment")
        print("3. Check balance")
        print("4. View history")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            account.apply_loan(amount)
        elif choice == "2":
            amount = float(input("Payment amount: "))
            account.make_payment(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.view_history()
        elif choice == "5":
            account.close()
            print("Logged out.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()

