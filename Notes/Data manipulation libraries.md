# Modules

Modules are files containing Python code (variables, functions, classes, etc.). They provide a way of organizing the code for large Python projects into files and folders. The key benefit offered by modules is _namespaces_ - a module or a specific function/class/variable from a module has to imported before it can be used within a Python script or notebook. This provides _encapsulation_ and avoid naming conflicts between your code vs. a module, or across modules.

Example: math, numpy, scipy, matplotlib, sckikit-learn, etc

```python
import math
help(math.ceil) # it's the smallest integer function
```

> Output:

```bash
Help on built-in function ceil in module math:

ceil(x, /)
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.
```

```bash
math.ceil(1.5)
```

> Output:

```bash
2
```

## Exercise

Shaun is currently paying back a home loan for a house a few years go. The cost of the house was `$800,000`. Shaun made a down payment of `25%` of the cost, and financed the remaining amount using a 6-year loan with an interest rate of `7%` per year (compounded monthly). Shaun is now buying a car worth `$60,000`, which he is planning to finance using a 1-year loan with an interest rate of `12%` per annum. Both loans are paid back in EMIs. What is the total monthly payment Shaun makes towards loan repayment?

```python
import math


def emi_calc(amount, down_payment, userinput, duration):
    loanamount = amount - amount * down_payment / 100

    def home(rate, duration):
        rate = (7 / 100) / 12
        power = 1 + rate
        emi = (loanamount * rate * math.pow(power, duration)) / (math.pow(power, duration) - 1)
        return math.ceil(emi)

    def car(rate, duration):
        rate = (12 / 100) / 12
        power = 1 + rate
        emi = (loanamount * rate * math.pow(power, duration)) / (math.pow(power, duration) - 1)
        return math.ceil(emi)

    if userinput == 'car':
        return car(0, duration)
    elif userinput == 'home':
        return home(0, duration)
    else:
        print("Invalid loan type")
        return 0


def data(userinput):
    print("\nEnter", userinput, "loan details:")

    amount = float(input("Enter total product value: $"))
    down_payment = float(input("Enter downpayment (%): "))
    duration = int(input("Enter duration (months): "))

    emi = emi_calc(amount, down_payment, userinput, duration)
    total_paid = emi * duration

    print("Monthly EMI: $%d" % emi)
    print("Total EMI paid: $%d" % total_paid)

    return total_paid


print("Enter details for both loans:")

car_total = data('car')
home_total = data('home')

print("\nTotal EMI paid (home + car) is: $%d" % (car_total + home_total))
```

> Output:

```bash
Enter details for both loans:

Enter car loan details:
Enter total product value: $60000
Enter downpayment (%): 0
Enter duration (months): 12
Monthly EMI: $5331
Total EMI paid: $63972

Enter home loan details:
Enter total product value: $800000
Enter downpayment (%): 25
Enter duration (months): 72
Monthly EMI: $10230
Total EMI paid: $736560

Total EMI paid (home + car) is: $800532                                                                                                 
```

Rahul takes:

- Home loan: $700,000, 25% down payment, 20 years, 7.5% p.a.

- Car loan: $50,000, no down payment, 3 years, 13% p.a.

👉 **Find:**

- Total amount paid for each loan

- Total interest paid overall

---

```python
import math
def emi_calc(amount,annual_rate,duration):
    rate = annual_rate/12
    emi = (amount * rate * math.pow(1+rate, duration)) / (math.pow(1+rate, duration) - 1)
    return math.ceil(emi)
home_cost = 700000
home_down_payment = 0.25*home_cost
home_loan = home_cost - home_down_payment
house_emi = emi_calc(home_loan, 0.075, 240)
home_total = house_emi * 240
house_interest = home_total - home_loan
car_loan = 50000
car_emi = emi_calc(car_loan, 0.13, 36)
car_total = car_emi * 36
car_interest = car_total - car_loan
print("\n-----FINAL-----")
print("HOME--->")
print("House EMI: %.2f"%house_emi)
print("Home total paid: %.2f"%home_total)
print("Home interest: %.2f"%house_interest)
print("CAR--->")
print("Car EMI: %.2f"%car_emi)
print("Car total paid: %.2f"%car_total)
print("Car interest: %.2f"%car_interest)
print("Total interest; %.2f"%(house_interest + car_interest))
print("\n------DONE------")
```

> Output:

```bash
-----FINAL-----
HOME--->
House EMI: 4230.00
Home total paid: 1015200.00
Home interest: 490200.00
CAR--->
Car EMI: 1685.00
Car total paid: 60660.00
Car interest: 10660.00
Total interest; 500860.00

------DONE------
```

## Exercise

**Travel Data:**

Paris (200,20,200), London (250,30,120), Dubai (370,15,80), Mumbai (450,10,70)

_(Flight, Hotel/day, Car/week)_

**Q1:** Cheapest city for 7 days

**Q2:** Cheapest city for 4, 10, 14 days

**Q3:** Budget = 1000 → max stay city

**Q4:** Budgets = 600, 1500, 2000 → max stay city + days

```python
cities = {
    "Paris": (200,20,200),
    "London": (250,30,120),
    "Dubai": (370,15,80),
    "Mumbai": (450,10,70)
}
def total_cost(city,days):
    flight, hotel, car = cities[city]
    return flight + (days * hotel) + car
print("Question-1 - 1 week trip min cost:")
days = 7
min_cost = float('inf')
best_city = ""
for city in cities:
    cost = total_cost(city, days)
    if cost < min_cost:
        min_cost = cost
        best_city = city
print("Best city is %s"%best_city, "and total cost: %d"%min_cost)
print("Question-2 - 4 days/10 days/2 weeks:")
list_days = [4,10,14]
for i in list_days:
    days = i
    min_cost = float('inf')
    best_city = ""
    for city in cities:
        cost = total_cost(city, days)
        if cost < min_cost:
            min_cost = cost
            best_city = city
    print("Best city for %d days trip is %s" %(days, best_city), "with total expenses of %d" % min_cost)
print("Question-3 : Maximize the duration:")
budget = 1000
max_days = 0
best_city = ""
for city in cities:
    flight, hotel, car = cities[city]
    remaining = budget - (flight + car)
    if remaining >0:
        days = remaining // hotel
        if days > max_days:
            max_days = days
            best_city = city
print("Maximum stay city is %s"%best_city, "with %d days"%max_days)
print("Question-4 : Plan change on budget change:")
budget_list = [600,2000,1500]
for i in budget_list:
    max_days = 0
    best_city = ""
    for city in cities:
        flight, hotel, car = cities[city]
        remaining = i - (flight + car)
        if remaining >0:
            days = remaining // hotel
            if days > max_days:
                max_days = days
                best_city = city
    print("Maximum stay city is %s"%best_city, "with %d days"%max_days, "for budget %d"%i)
```

> Output:

```bash
Question-1 - 1 week trip min cost:
Best city is Paris and total cost: 540
Question-2 - 4 days/10 days/2 weeks:
Best city for 4 days trip is Paris with total expenses of 480
Best city for 10 days trip is Paris with total expenses of 600
Best city for 14 days trip is Dubai with total expenses of 660
Question-3 : Maximize the duration:
Maximum stay city is Mumbai with 48 days
Question-4 : Plan change on budget change:
Maximum stay city is Paris with 10 days for budget 600
Maximum stay city is Mumbai with 148 days for budget 2000
Maximum stay city is Mumbai with 98 days for budget 1500
```

---

---

  

[[Section - 4 - Numpy]]

[[Section - 5 Pandas]]
