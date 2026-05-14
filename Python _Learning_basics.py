marks = [78, 85, 90, 66]
average = sum(marks) / len(marks)
print(average)

print("Hello Python")

print("Ramanan")
print("murugan")
print("i will practice daily")


city = "cumbum"
state = "tamil_nadu"
pincode = "625516"
print(city,state,pincode)


score = 85

if score >= 90:
    print("A Grade")
elif score >= 80:
    print("B Grade") 
elif score >= 70:
    print("C Grade")
elif score >= 60:
    print("D Grade")
else:
    print("Fail")


for i in range(1, 6):
    print(i)


prices = [240, 245, 242, 250, 248]
for price in prices:
    if price > 245:           # Filter
        print(f"Buy signal: {price}")
    elif price < 242:         # Sell
        print(f"Sell signal: {price}")


# Count up
i = 0
while i < 5:
    print(i)
    i += 1     # Don't forget this!


# Type this in your hello.py file and run it
print("Hello, world!")
print("My name is Python")
print(2 + 3)


# Creating variables
name = "Rahul"
age = 28
salary = 45000.50
is_employed = True

# Using variables in print()
print(name)
print(age)
print("My name is", name)
print(f"I am {age} years old")  # f-string — very useful!

# Exercise 1: Print your name and city
name = "Ramanan" 
age = 23
print(f"My Name is {name} and my {age}")


# Simple salary calculator
monthly_salary = 30000
months = 12
annual_salary = monthly_salary * months
print(f"annual_salary:{annual_salary}")

# What will this print?
x = 10
y = 3
print(x+y)
print(x-y)
print(x*y)

# Data types

# 1. int — whole numbers
age = 25
employees = 1500

# 2. float — decimal numbers
price = 99.99
tax_rate = 0.18

# 3. str — text (always in quotes)
name = "Priya"
city = 'Chennai'  # single or double quotes, both work

# 4. bool — True or False only
is_active = True
has_discount = False

# Check the type of any variable
print(type(age))      # <class 'int'>
print(type(price))    # <class 'float'>
print(type(name))     # <class 'str'>
print(type(is_active)) # <class 'bool'>

# Arithmetic operators 
a = 10
b = 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.333... — division (always float)
print(a // b)  # 3   — floor division (no decimal)
print(a % b)   # 1   — remainder (modulo)
print(a ** b)  # 1000 — power (10³)

# Comparison operators and  Logical operators 
sales = 5000
target = 4500

print(sales > target)   # True
print(sales < target)   # False
print(sales == target)  # False  (== means "equal to", not =)
print(sales != target)  # True   (not equal)
print(sales >= 5000)    # True

# Logical operators combine conditions
age = 30
salary = 60000

print(age > 25 and salary > 50000)  # True — both must be true
print(age > 25 or salary > 80000)   # True — at least one true
print(not age > 25)                  # False — flips the result



# str → int (text to whole number)
age_text = "28"
age_num = int(age_text)
print(age_num + 2)         # 30 — now you can do maths

# str → float (text to decimal number)
price_text = "1299.99"
price_num = float(price_text)
print(price_num * 1.18)    # 1533.9882 (with GST)

# int → str (number to text — needed to join with other text)
year = 2024
print("Year: " + str(year))  # "Year: 2024"
# print("Year: " + year) ← ERROR! Cannot join str and int directly

# float → int (removes decimal, does NOT round — it truncates)
print(int(9.9))   # 9  (not 10 — decimal is dropped)
print(int(3.1))   # 3

# round() — for proper rounding
print(round(9.6))         # 10
print(round(3.14159, 2))  # 3.14 (2 decimal places)

# Check before converting — avoid errors
value = "abc"
# int(value) ← This WILL crash — "abc" cannot become a number
# Always make sure the value can convert before you do it


# Billing calculator
unit_price = 450
quantity= 12
discount= 0.10
gst_rate= 0.18

subtotal = unit_price * quantity
discount_amount = subtotal * discount
after_discount = subtotal - discount_amount
gst_amount = after_discount * gst_rate
final_bill = after_discount + gst_amount

print(f"Subtotal:        {subtotal}")
print(f"Discount:       -{discount_amount}")
print(f"After discount:  {after_discount}")
print(f"GST (18%):       {gst_amount}")
print(f"Final bill:      {round(final_bill, 2)}")


# Original has 2 problems:
# 1. score is a string — can join text but cannot do score + 5
# 2. score + 5 fails because you can't add str and int

score_text = "95"
score_num = int(score_text)

print("Your score is " + score_text + " out of 100")  # text join — fine
print(score_num + 5)   # 100 — maths needs the number version

# Creating lists - use square brackets []
monthly_salary = [42000,38000,51000,47000,55000,49000]
regions = ["North","South","East","West"]
mixed = ["arun",28,True,55000.0] # lists can hold differnt types
emply_list = [] # an emplty list - add items 

# Undestanding indexes 
# Understanding indexes
#         [0]     [1]     [2]     [3]     [4]     [5]
# sales = [42000, 38000, 51000, 47000, 55000, 49000]
#         [-6]    [-5]    [-4]    [-3]    [-2]    [-1]

# Access by positive indext(form start)
print(monthly_salary[0]) # 42000 — first item
print(monthly_salary[3])   # 38000 — second item
print(monthly_salary[5])  # 49000 — sixth (last) item


# Access by negative index (from end) — very handy
print(monthly_salary[-1])  # 49000 — last item
print(monthly_salary[-2])  # 55000 — second to last

# Length of a list
print(len(monthly_salary))  # 6

#Slicing
sales = [42000, 38000, 51000, 47000, 55000, 49000]
#index:   0       1       2       3       4       5

# [start:end] — start included, end NOT included
print(sales[0:3])    # [42000, 38000, 51000] — indexes 0,1,2
print(sales[2:5])    # [51000, 47000, 55000] — indexes 2,3,4

# Omit start → begins from index 0
print(sales[:3])     # [42000, 38000, 51000] — first 3 items

# Omit end → goes to last item
print(sales[3:])     # [47000, 55000, 49000] — from index 3 onward

# Last N items using negative
print(sales[-3:])    # [47000, 55000, 49000] — last 3 items
print(sales[-2:])    # [55000, 49000] — last 2 items

# First half / second half
half = len(sales) // 2
print(sales[:half])   # [42000, 38000, 51000] — first half
print(sales[half:])   # [47000, 55000, 49000] — second half

# Modifying Lists:
# Starting list
products = ["Laptop", "Mouse", "Keyboard"]

# ADD items
products.append("Monitor")         # adds to END: [..., "Monitor"]
products.insert(1, "Webcam")      # adds at index 1, shifts rest right
print(products)
# ["Laptop", "Webcam", "Mouse", "Keyboard", "Monitor"]

# REMOVE items
products.remove("Mouse")           # removes FIRST match by value
last = products.pop()               # removes and RETURNS last item
second = products.pop(1)           # removes and returns item at index 1

# CHANGE an item
products[0] = "Desktop PC"          # replace first item

# SORT a list
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()                       # sorts in place: [1,2,3,5,8,9]
sorted_copy = sorted(numbers)       # returns new sorted list, original unchanged
numbers.sort(reverse=True)          # descending: [9,8,5,3,2,1]

# Built-in math functions on numeric lists
sales = [42000, 38000, 51000, 47000]
print(sum(sales))                   # 178000 — total
print(max(sales))                   # 51000  — highest
print(min(sales))                   # 38000  — lowest
print(sum(sales) / len(sales))      # 44500  — average

monthly = [41000,38000,52000,47000,55000,49000,61000,58000,53000,44000,48000,67000]
q1 = monthly[:3]
q2 = monthly[3:6]
q3 = monthly[6:9]
q4 = monthly[9:]

print(f"Q1 total: {sum(q1)}")
print(f"Q2 total: {sum(q2)}")
print(f"Q3 total: {sum(q3)}")
print(f"Q4 total: {sum(q4)}")

quarters = [sum(q1), sum(q2), sum(q3), sum(q4)]
print(f"Best quarter total: {max(quarters)}")

#Tuples:
# No adding, no removing, no swapping.

# A Tuple representing a fixed record (Name, ID, Salary)
employee_record = ("John Doe", 1005, 50000)

# 1. Accessing data works just like a list
print(f"Employee Name: {employee_record[0]}")
print(f"Monthly Salary: {employee_record[2]}")

# dictionaries:
# Creating a dictionary — curly braces, key: value pairs
employee={"name":"Ramanan",
            "age": 23,
            "department": "analytics",
            "salary": 140000,
            "is_active": True}

# Accessing values by key
print(employee["name"])                # "Ramanan"
print(employee["salary"])              # 140000

#.get() — safer access (no error if key doesn't exist)
# print(employee["city"])   # None (key doesn't exist, no crash)
print(employee.get("city", "defalet"))  # "N/A" (default if key missing)

# Adding a new key 
employee["city"] = 'coimbatore'

# Updating an existing key
employee["salary"] = 82000

# Removing a key
del employee["age"]

# Useful dictionary methods
print(employee.keys())     # all keys: dict_keys(["name","department",...])
print(employee.values())   # all values
print(employee.items())    # key-value pairs as tuples
print("salary" in employee)  # True — check if key exists


# list of dictionaries
# The most important pattern in Python data work: 
# a list of dictionaries represents a table — exactly like database rows or a DataFrame.

employees =[
    {"name": "Arun",    "dept": "Sales",     "salary": 55000, "rating": "good"},
    {"name": "Priya",   "dept": "Analytics", "salary": 75000, "rating": "excellent"},
    {"name": "Ravi",    "dept": "Sales",     "salary": 48000, "rating": "average"},
    {"name": "Divya",   "dept": "IT",        "salary": 68000, "rating": "excellent"},]


# Access a specific "cell": list[row_index]["column_key"]
print(employees[0]["name"])      # "Arun"    — row 0, name column
print(employees[1]["salary"])   # 75000    — row 1, salary column
print(employees[-1]["dept"])    # "IT"     — last row, dept column

# Get ALL salaries as a list (this pattern is called list comprehension)
all_salaries = [emp["salary"] for emp in employees]
print(all_salaries)               # [55000, 75000, 48000, 68000]
print(f"Average salary: {sum(all_salaries)/len(all_salaries)}")

# Problem: find unique values in a list with duplicates
cities = ["Chennai", "Coimbatore", "Chennai", "Bangalore",
          "Coimbatore", "Hyderabad", "Chennai"]

# Convert list to set → removes all duplicates instantly
unique_cities = set(cities)
print(unique_cities)         # {'Chennai', 'Coimbatore', 'Bangalore', 'Hyderabad'}
print(len(unique_cities))    # 4

# Check membership — much faster than in a list
print("Chennai" in unique_cities)    # True
print("Mumbai" in unique_cities)     # False

# Set operations — very useful for data comparisons
q1_customers = {"A", "B", "C", "D"}
q2_customers = {"C", "D", "E", "F"}

new_customers = q2_customers - q1_customers           # {'E', 'F'} — in Q2 not Q1
old_customers = q1_customers - q2_customers  
retained = q1_customers & q2_customers                 # {'C', 'D'} — in BOTH
all_customers = q1_customers | q2_customers            # all unique customers
print(f"New customers: {new_customers}")
print(f"Old customers: {old_customers}")
print(f"Retained: {retained}")
print(f"Total unique: {len(all_customers)}")
print(f"Total unique: {all_customers}")

# Exercise: Customer transaction summary
transactions = [
    {"customer": "Arun",  "product": "Laptop",  "amount": 45000, "paid": True},
    {"customer": "Priya", "product": "Phone",   "amount": 22000, "paid": False},
    {"customer": "Ravi",  "product": "Tablet",  "amount": 18000, "paid": True},
    {"customer": "Arun",  "product": "Mouse",   "amount": 1500,  "paid": True},
]
total_revenue = sum(t["amount"] for t in transactions)
unique_customers = set(t["customer"] for t in transactions)
paid_customers = [t["customer"] for t in transactions if t["paid"]]
print(f"Transactions: {len(transactions)}")
print(f"Revenue: {total_revenue}")
print(f"Unique customers: {unique_customers}")
print(f"Paid: {paid_customers}")

# Basic if / elif / else structure
salary_1 = 72000
if salary_1 >= 100000:
    print("platinum-oustanding !")
    print("bonus: 25%")
elif salary_1 >= 75000:
    print("Gold- greant performance")
    print("bouns:15%")
elif salary_1 >= 5000:
    print("silver-good effort")
    print("bonus:10%")
else:
    print("need improvement")
    price("no bonus this quarter")

# multiple coditions with and / or
age_1 = 28
experience = 5
degree = "MBA"

if age_1 >= 25 and experience >= 3 and degree == "MBA":
    print("eligible for manager role")
elif age >= 25 and experience >= 5:
    print("Eligible for senior analyst role")
else:
    print('keep gaining experience')

# for loop
# Basic for loop — variable "sale" gets each value one by one
monthly_sales = [42000,38000,51000,47000]
print(monthly_sales)

for sale in monthly_sales:
        print(f"sale this month: {sale}")

# Combining loop + if — filter items
print("------High performing months ----")

for sale in monthly_sales:
    if sale in monthly_sales:
        if sale >= 45000:
            print(f"High: {sale}")
        else:
            print(f"Low: {sale}")

# enumerate() — get the index AND value together
print("---Monthly report---")
for month_num,sale in enumerate(monthly_sales,start=1):
    print(f"month{month_num}:{sale}")

# Loop through a dictionary's items
employee_2 = {"name":"priya","dept":"analystics","salary":77000}
for key,value in employee_2.items():
    print(f"{key}:{value}")
    
# range() — loop a specific number of times
for i in range(5):          # i goes: 0, 1, 2, 3, 4
    print(f"Loop number {i}")

for i in range(1, 6):       # i goes: 1, 2, 3, 4, 5
    print(i)

# While loop — runs as long as condition is True
# Use when you don't know how many times you'll loop
balance = 0
month = 0
monthly_deposit = 8000
target = 100000

while balance < target:
    balance += monthly_deposit
    month += 1
    print(f"Month {month}: Balance = {balance}")

print(f"Reached target in {month} months!")

# break — exit the loop early when a condition is met
sales_1 = [42000,38000,51000,29000,47000]
for i,sale in enumerate(sales_1):
    if sale < 35000:
        print(f"warning at month {i+1}: sale {sale}is below minimum")
        break 


# Employee grade report

employees = [
    {"name": "Arun",  "salary": 55000},
    {"name": "Priya", "salary": 75000},
    {"name": "Ravi",  "salary": 48000},
    {"name": "Divya", "salary": 82000},
]
grade_a_count = 0

for emp in employees:
    if emp["salary"] >= 70000:
        grade = "A"
        grade_a_count += 1
    elif emp["salary"] >= 50000:
        grade = "B"
    else:
        grade = "C"
    print(f"{emp['name']:10} | {emp['salary']:6} | Grade: {grade}")

print(f"Grade A employees: {grade_a_count}")



# function 
# STEP 1: Define the function (write it once)
def greet():
    print("hello!")
    print("Welcome.")
# STEP 2: Call the function (run it)
greet()
greet()

# Function with INPUT (parameters)
def greet_person(name,role):
    print(f"Hello {name}, Welcome to the {role} team!")

greet_person("Arun","Analytics")
greet_person("priya","sales")

# Without return — just does something
def show_salary(salary):
    print(f"Salary: {salary}")       # prints but returns nothing

# With return — produces a value
def calculate_gst(price, rate=0.18):   # rate has a DEFAULT value
    gst = price * rate
    return gst  

#Use the returned value 
tax = calculate_gst(1000)            # tax = 180.0
luxury_tax = calculate_gst(5000,0.28)         # custom rate
print(f"standard GST: {tax}")
print(f"Luxury GST: {luxury_tax}")
print(f"Final price: {1000 + tax}")   # use directly in expression

# Return multiple values :
def sales_summary(sales_list):
    total= sum(sales_list)
    average = total/len(sales_list)
    best= max(sales_list)
    worst = min(sales_list)
    return total, average, best, worst

sale =[42000, 51000, 38000, 67000, 45000]
total, avg, best, worst = sales_summary(sale)
print(f"Total:{total} | Average: {avg} | Best: {best} | Worst: {worst}")

# payslip calculator
def generate_payslip(name, basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.15
    gross = basic_salary + hra + da
    tax = gross * 0.10
    net = gross - tax
    return{
        "name": name,
        "basic": basic_salary,
        "hra": hra,
        "da": da,
        "gross": gross,
        "tax": tax,
        "net_salary": net
}

payslip = generate_payslip("Arun", 50000)
for key,val in payslip.items():
    print(f"{key:12}: {val}")

# sales_report
# ============================================
#   SALES REPORTING SYSTEM — Week 1 Project
# ============================================

#---DATA---
# A list of dictionares = our "database table"
sales_records =[
    {"rep":"Arun",  "region": "South", "product": "Laptop", "amount": 85000, "month": "Jan"},
    {"rep":"Priya",  "region": "North", "product": "Phone", "amount": 62000, "month": "Jan"},
    {"rep":"Ravi",  "region": "South", "product": "Tablet", "amount": 41000, "month": "Feb"},
    {"rep":"Divya",  "region": "East", "product": "Laptop", "amount": 97000, "month": "Feb"},
    {"rep":"Arun",  "region": "South", "product": "Phone", "amount": 55000, "month": "Feb"},
    {"rep":"Karthik",  "region": "West", "product": "Tablet", "amount": 73000, "month": "Mar"},
    {"rep":"Priya",  "region": "North", "product": "Laptop", "amount": 91000, "month": "Mar"},
    {"rep":"Ravi",  "region": "South", "product": "Phone", "amount": 38000, "month": "Mar"}

]

#---FUNCTIONS----

def get_perfomance_grade(amount):
     # """Returns a grade based on sale amount"""
     if amount >= 90000: return "S" #super
     elif amount >= 70000: return "A" #excellent
     elif amount >= 50000: return "B" #good 
     else:                 return "c"  #need work
    
def total_by_rep(records,rep_name):
    # """Total sales for one rep"""
    total = 0
    for record in records:
        if record["rep"] == rep_name:
            total += record["amount"]
    return total 

def total_by_region(records,region_name):
     # """Total sales for one region"""
    return sum(r["amount"] for r in records if r["region"] == region_name)


# --- MAIN REPORT ---

print("=" * 55)
print("      QUARTERLY SALES REPORT - Q1 2024")
print("=" * 45)


# 1. Print all transactions with grade 
print(f"{'Rep':<10} {'Region':<10} {'Product':<8} {'Amount':>8} {grade}")
print("-" * 45)
for rec in sales_records:
    grade = get_perfomance_grade(rec["amount"])
    print(f"{rec['rep']:<10} {rec['region']:<8} {rec['product']:<8} {rec['amount']:>8,} [{grade}]")


# 2. Summary statistics
all_amounts = [r["amount"] for r in sales_records]
print(f"Total revenue:   {sum(all_amounts):>10,}")
print(f"Aveage sale:   {sum(all_amounts)//len(all_amounts):>10,}")
print(f"best sale:   {max(all_amounts):>10}")
print(f"Worst sale:    {min(all_amounts):>10,}")

# 3. Sales by rep
print("" \
"---- By Sales Rep ----")
reps = set(r["rep"] for r in sales_records)
for rep in sorted(reps):
    total = total_by_rep(sales_records,rep)
    print(f"   {rep:<10}: {total:>8,}")

# 4. Sales by region
print("------By Region -----")
regions = set(r["region"] for r in sales_records)
for region in sorted(regions):
    total= total_by_region(sales_records,region)
    print(f"    {region:>8}: {total:>8,}")

print("" + "=" * 55)
