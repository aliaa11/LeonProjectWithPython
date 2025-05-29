from db import Database

class LoanAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()

    def apply_loan(self, amount):
        self.db.execute(
            "UPDATE users SET loan_amount = loan_amount + %s WHERE id = %s",
            (amount, self.user_id)
        )
        print(f"Loan of {amount} added.")

    def make_payment(self, amount):
        self.db.execute("SELECT loan_amount FROM users WHERE id = %s", (self.user_id,))
        loan = self.db.fetchone()[0]

        if amount > loan:
            print("Payment exceeds your balance.")
        else:
            self.db.execute(
                "UPDATE users SET loan_amount = loan_amount - %s WHERE id = %s",
                (amount, self.user_id)
            )
            self.db.execute(
                "INSERT INTO payments (user_id, amount) VALUES (%s, %s)",
                (self.user_id, amount)
            )
            print("Payment successful.")

    def check_balance(self):
        self.db.execute("SELECT loan_amount FROM users WHERE id = %s", (self.user_id,))
        balance = self.db.fetchone()[0]
        print(f"Your balance is: {balance}")

    def view_history(self):
        self.db.execute(
            "SELECT amount, payment_date FROM payments WHERE user_id = %s ORDER BY payment_date",
            (self.user_id,)
        )
        payments = self.db.cur.fetchall()
        print("Payment History:")
        for amount, date in payments:
            print(f"{date} - {amount}")

    def close(self):
        self.db.close()
