from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, email, phonenumber, age, income, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.age = age
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 25000:
            return False
        return True

    def display_customer(self):
        print("\nCustomer Details")
        print("----------------")
        print("Customer ID  :", self.customer_id)
        print("Name         :", self.name)
        print("Email        :", self.email)
        print("Phonenumber  :", self.phonenumber)
        print("Age          :", self.age)
        print("Income       :", self.income)
        print("Credit Score :", self.credit_score)


class Loan(ABC):
    def __init__(self, loan_id, customer, loan_amount, interest_rate, tenure):
        self.loan_id = loan_id
        self.customer = customer
        self.__loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.__balance = loan_amount
        self.__total_paid = 0
        self.repayment_history = []
        self.status = "Applied"

    @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):
        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False
        return True

    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application was rejected")
            return

        if not self.check_loan_eligibility():
            print("Customer is not eligible")
            return

        self.status = "Sanctioned"
        print("\nLoan sanctioned successfully")

    def repay(self, amount):
        if self.status != "Sanctioned":
            print("Repayment not allowed")
            return

        if amount <= 0:
            print("Invalid amount")
            return

        if amount > self.__balance:
            print("Amount exceeds balance")
            return

        self.__balance -= amount
        self.__total_paid += amount
        self.repayment_history.append(amount)

        print("\nPaid:", amount)
        print("Balance:", self.__balance)

        if self.__balance == 0:
            self.status = "Closed"
            print("Loan closed")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):
        print("\n=== LOAN STATEMENT ===")
        print("Loan ID:", self.loan_id)
        print("Customer:", self.customer.name)
        print("Loan Amount:", self.__loan_amount)
        print("Balance:", self.__balance)
        print("Status:", self.status)

        print("\nRepayments:")
        for i, amt in enumerate(self.repayment_history, 1):
            print(f"{i}. {amt}")

    def __str__(self):
        return f"{self.loan_id} | {self.customer.name} | {self.status}"


class HomeLoan(Loan):
    def calculate_emi(self):
        p = self.get_loan_amount()
        r = self.interest_rate / (12 * 100)
        n = self.tenure * 12

        emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
        return round(emi, 2)


# Create Customers
Dedeepya = Customer(1, 'Dedeepya', 'dedeepya@gmail.com', 9876543210, 21, 50000, 750)
sai = Customer(2, 'Sai', 'sai@gmail.com', 9876543210, 21, 60000, 600)

Dedeepya.display_customer()
print("Eligibility:", Dedeepya.check_eligibility())

sai.display_customer()
print("Eligibility:", sai.check_eligibility())

# Create Loan (correct)
home_loan = HomeLoan("HL1001", Dedeepya, 500000, 8.5, 10)

print("\nLoan Application")
print(home_loan)

if home_loan.check_loan_eligibility():
    home_loan.sanction_loan()

    print("\nEMI:", home_loan.calculate_emi())

    home_loan.repay(100000)
    home_loan.repay(150000)
    home_loan.repay(250000)

else:
    print("Not eligible")

print("\nFinal Details:")
print(home_loan)

home_loan.display_statement()
