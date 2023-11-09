'''
- Methods which performs operation on external data
- It can also perform operation on class data
- No need to pass object or class reference
- Created using decorator '@staticmethod'

'''

class Bank:
    bank_name = 'Kotak Mahindra'
    rate_of_interest = 12.25

    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        print(si)

prin= float( input("Enter the principle amount:"))
n= int( input("Enter number of years:"))

Bank.simple_interest(prin,n)