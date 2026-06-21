# # # # # def my_function_with_arguments(username,greetings):
# # # # # 		print("Hello %s, %s"%(username,greetings))
# # # # # my_function_with_arguments('Burger','I hope you are fine')
# # # # def sum_two_numbers(a, b):
# # # #     return a + b
# # # # print(sum_two_numbers(4,5))
# # # def list_benefits(organized):
# # #     print("More organized code")
# # #     print("More readable code")
# # #     print("Easier code reuse")
# # #     print("Allowing programmers to share and connect code together")
# # #     return
# # # list_benefits('burhe')
# # def list_benefits():
# #     return [
# #         "More organized code",
# #         "More readable code",
# #         "Easier code reuse",
# #         "Allowing programmers to share and connect code together"
# #     ]
# # def build_sentence(info):
# #     return info + " is a benefit of functions!"
# # def name_of_benefits_of_functions():
# #     list_of_benefits = list_benefits()
# #     for benefits in list_of_benefits:
# #         print(build_sentence(benefits))
# # name_of_benefits_of_functions()
# # Radha is planning to buy a house that costs $1,260,000. She is  considering two options to finance her purchase:
# #
# #     Option 1: Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.
# #     Option 2: Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount.
# #
# # Both these loans have to paid back in equal monthly installments (EMIs). Which loan has a lower EMI among the two?
# def calc_emi(amount):
#     emi = amount/12
#     return "Emi is %.2f"%emi
# print("Option 1: Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.\nOption 2: Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount.")
# user = int(input("Enter your option: "))
# if user == 1:
#     amount = float(input("Enter amount: "))
#     print(calc_emi(amount))
# elif user == 2:
#     amount = float(input("Enter amount: "))
#     amount -= 300000
#     print("Amount after down payment : %.2f"%amount)
#     print(calc_emi(amount))
# suppose rate is 1.2% and number of months is 36, then:
# import math
# def calc_emi(amount,duration):
#     rate = (12/1000)
#     power = 1+rate
#     emi = (amount*rate*(math.pow(power,duration)))/(math.pow(power,duration)-1)
#     return "EMI per month is: %.2f"%emi
# amount = float(input("Enter amount: "))
# duration = int(input("Enter number of months: "))
# print(calc_emi(amount,duration))
