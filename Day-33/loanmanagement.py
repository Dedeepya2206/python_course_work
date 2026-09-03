from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, email, phonenumber, age, income, credit_score):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        self.age=age
        self.income=income
        self.credit_score=credit_score

    def check_eligibility(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 25000:
            return False
        return True
    
    def display_customer(self):
        print("\nCustomer Details")
        print("- - - - - - - - - - - ")
        print("Customer ID :", self.customer_id)
        print("Name :", self.name)
        print("email :", self.email)
        print("phonenumber :", self.phonenumber)
        print("age :", self.age)
        print("income :", self.income)
        print("credit_score :", self.credit_score)


Dedeepya = Customer(1,"Dedeepya","dedeepya@gmail.com", 9876543210,23,50000,750)
Dedeepya.display_customer()
print("Eligibility", Dedeepya.check_eligibility())

sai = Customer(2,"Sai","sai@gmail.com", 9872345910,23,4000,750)
sai.display_customer()
print("Eligibility", sai.check_eligibility())


#LOAN MANAGEMENT
class Loan(ABC):
    def __init__(self,loan_id,customer,loan_amount,interest_rate,tenure):
        self.loan_id=loan_id
        self.customer=customer
        self.__loan_amount=loan_amount
        self.intrest_rate=interest_rate
        self.tenure=tenure
        self.__balance=loan_amount
        self.__total_paid=0
        self.repayment_history=[]
        self.status="Applied"
    @abstractmethod
    def calculate_emi(self):
        pass
    def check_loan_eligibility(self):
        if not self.customer.check_eligibility():
            self.status="Rejected"
            return False
        return True
    def sanction_loan(self):
        if self.status=="Rejected":
            print("Loan application was Rejected")
            return
        if  not self.check_loan_eligibility():
            print("Customer is not eligible for the loan")
            return
        self.status="Sanctioned"
        print("\nLoan sanctioned successfully")
    def repay(self, amount):
        if self.status != "Sanctioned":
            print("Repayment is not allowed")
            print("Loan status :", self.status)
            return
        if amount <=0:
            print("Invalid repayment amount")
            return

        if amount > self.__balance:
            print("Repayment amunt is greater than outstanding balance")
            return

        self.__balance -=amount
        self.__total_paid +=amount
        self.repayment_history.append(amount)
        print("\nRepayment successful")
        print("Amount Paid :", amount)
        print("Outstanding Balance :", self.__balance)

        if self.__balance == 0:
            self.status = "Closed"
            print("Loan Closed ")
        def get_balance(self):
            return self.__balance
        def get_loan_amount(self):
            return self.__loan_amount
        def get_total_paid(self):
            return self.__total_paid
        def display_statement(self):
            print("\n")
            print("="*40)
            print("LOAN STATEMENT")
            print("="*40)
            print("Loan ID          :", self.loan_id)
            print("Customer Name    :", self.customer.name)
            print("Loan Amount      :", self.__loan_amount)
            print("Intrest Rate     :", self.interest_rate)
            print("Tenure           :", self.Tenure)
            print("Total Paid       :", self.__total_paid)
            print("Outstanding Balance :", self.__balance)
            print("Loan Status       :", self.status)
            print("\nRepayment History")

            if not self.repayment_history:
                print("No repayments made")
            else:
                for i in range(len(self.repayment_history)):
                    print(f"Payment {i+1}       : {self.repayment_history[i]}")
                print("=" *40)
        def __str__(self):
            return(
                f"Loan ID: {self.loan_id},"
                f"Customer: {self.customer_name},"
                f"Loan Amount: {self.__loan_amount}",
                f"Outstanding: {self.__balance}",
                f"Status: {self.status}"
                )
    


        

