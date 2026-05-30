
# File I/O & CSV handling - COMPLETE WITH ANSWERS

# ============================================
# SECTION 1: FILE OPERATIONS BASICS
# ============================================

# METHOD 1: Basic open/close (you must close manually)
file = open("data.txt","r") # r- read mode
content = file.read()
file.close()    # MUST close - or data stays locked

# METHOD 2: with open()- ALWAYS use this (auto-closes)
with open("data.txt","r") as file:
    content = file.read()

# file is automatically closed when the with block ends
print(content)

# File modes - what the second argument means 
# "r" - read only (file must exist)
# "w" - write (creates new file or overwrites existing)
# "a" - append (add to end of existing file)
# "r+" - read and write 

# ============================================
# SECTION 2: READING FILES (3 METHODS)
# ============================================

# First, create a test file to work with 
# (Run this once to create the file)
with open("employees.txt","w") as f:
    f.write("Arun,Sales,55000\n")
    f.write("Priya,Analyst,75000\n")
    f.write("Ravi,IT,68000\n")
    f.write("Divya,Sales,52000\n")

# newline character (like pressing Enter in a text file)

# READ METHOD 1: read() - entire file as one big string
print("\n=== METHOD 1: read() ===")
with open("employees.txt","r") as f:
    all_text = f.read()
print(all_text)
print(f"Type: {type(all_text)}")
# OUTPUT: 
# Arun,Sales,55000
# Priya,Analyst,75000
# Ravi,IT,68000
# Divya,Sales,52000
# Type: <class 'str'>

# READ METHOD 2: readlines() - list of lines (each line = one string)
print("\n=== METHOD 2: readlines() ===")
with open("employees.txt","r") as f:
    lines = f.readlines()
print(lines)
print(f"First line: {lines[0]}")
print(f"First line stripped: {lines[0].strip()}")
# OUTPUT:
# ['Arun,Sales,55000\n', 'Priya,Analyst,75000\n', 'Ravi,IT,68000\n', 'Divya,Sales,52000\n']
# First line: Arun,Sales,55000
# First line stripped: Arun,Sales,55000

# READ METHOD 3: iterate line by line - best for large files
print("\n=== METHOD 3: iterate line by line ===")
with open("employees.txt","r") as f:
    for line in f:
        clean = line.strip()
        parts = clean.split(",")
        print(f"Name: {parts[0]}, Dept: {parts[1]}, Salary: {parts[2]}")
# OUTPUT:
# Name: Arun, Dept: Sales, Salary: 55000
# Name: Priya, Dept: Analyst, Salary: 75000
# Name: Ravi, Dept: IT, Salary: 68000
# Name: Divya, Dept: Sales, Salary: 52000

# ============================================
# SECTION 3: WRITING FILES & CREATING CSVs
# ============================================

print("\n=== WRITING FILES ===")
results = [
    {"name":"Arun","score":88},
    {"name":"Priya","score":95},
    {"name":"Ravi","score":72},
]

with open("results.txt","w") as f:
    f.write("Name,Score,Grade\n")
    for r in results:
        grade = "A" if r["score"] >= 90 else "B" if r["score"] >=75 else "C"
        f.write(f"{r['name']},{r['score']},{grade}\n")

# OUTPUT in results.txt:
# Name,Score,Grade
# Arun,88,B
# Priya,95,A
# Ravi,72,C

# ============================================
# SECTION 4: READING CSV FILES WITH CSV MODULE
# ============================================

import csv

# First create a sample CSV to work with 
print("\n=== CREATING CSV FILE ===")
with open("sales.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Month","Region","Sales","Target"])
    writer.writerow(["jan","south",85000,80000])
    writer.writerow(["jan","north",62000,70000])
    writer.writerow(["feb","south",91000,80000])
    writer.writerow(["feb","north",77000,70000])

# Reading CSV - DictReader gives each row as a dictionary 
print("\n=== READING CSV WITH DictReader ===")
with open("sales.csv","r") as f:
    reader = csv.DictReader(f)      # header row becomes dict keys
    for row in reader:
        sales = int(row["Sales"])    # remember: CSV values are strings
        target = int(row["Target"])
        met = "✓" if sales >= target else "✗"
        print(f"{row['Month']}|{row['Region']}|{sales:,}|{met}")

# OUTPUT:
# jan|south|85,000|✓
# jan|north|62,000|✗
# feb|south|91,000|✓
# feb|north|77,000|✓

# ============================================
# SECTION 5: COMPLEX CSV PROCESSING
# ============================================

print("\n=== PRODUCTS CSV ANALYSIS ===")
# Step 1: Create CSV
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product","category","price","quantity"])
    writer.writerow(["Laptop","Electronics",45000,10])
    writer.writerow(["Mouse","Electronics",800,50])
    writer.writerow(["Desk","Furniture",12000,5])
    writer.writerow(["Chair","Furniture",8500,8])
    writer.writerow(["Keyboard","Electronics",1500,30])

# Step 2: Read and analyse
products = []
with open("products.csv", "r") as f:
    for row in csv.DictReader(f):
        products.append({
            "product": row["product"],
            "price": int(row["price"]),
            "quantity": int(row["quantity"]),
            "value": int(row["price"]) * int(row["quantity"])
        })

total_value = sum(p["value"] for p in products)
priciest = max(products, key=lambda p: p["price"])
cheapest = min(products, key=lambda p: p["price"])

print(f"Total products: {len(products)}")
print(f"Total inventory value: {total_value:,}")
print(f"Most expensive: {priciest['product']} at {priciest['price']:,}")
print(f"Cheapest: {cheapest['product']} at {cheapest['price']:,}")

# OUTPUT:
# Total products: 5
# Total inventory value: 691,000
# Most expensive: Laptop at 45,000
# Cheapest: Mouse at 800

# ============================================
# SECTION 6: ERROR TYPES & EXAMPLES
# ============================================

print("\n=== ERROR TYPES ===")

# ValueError - wrong type conversion 
try:
    int("abc")       # ValueError: invalid literal for int()
except ValueError:
    print("ERROR 1 - ValueError: Cannot convert 'abc' to int")

# KeyError - dictionary key doesn't exist
d = {"name": "Arun"}
try:
    d["salary"]       # KeyError: 'salary'
except KeyError:
    print("ERROR 2 - KeyError: 'salary' key doesn't exist")

# IndexError - list index out of range
lst = [1, 2, 3]
try:
    lst[5]        # IndexError: list index out of range 
except IndexError:
    print("ERROR 3 - IndexError: index 5 out of range")

# FileNotFoundError - file doesn't exist
try:
    open("ghost.csv")  # FileNotFoundError: no such file
except FileNotFoundError:
    print("ERROR 4 - FileNotFoundError: ghost.csv doesn't exist")

# ZeroDivisionError - dividing by zero
try:
    100 / 0          # ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("ERROR 5 - ZeroDivisionError: Cannot divide by zero")

# TypeError - wrong type for operation 
try:
    "hello" + 5      # TypeError: can only concatenate str to str
except TypeError:
    print("ERROR 6 - TypeError: Cannot add string and number")

# ============================================
# SECTION 7: TRY/EXCEPT/ELSE/FINALLY
# ============================================

print("\n=== TRY/EXCEPT/ELSE/FINALLY ===")

# BASIC: try/except
print("\n1. Basic try/except:")
try:
    value = int("abc")     # this will fail
    print(value)
except ValueError:
    print("   → Could not convert to number")   # runs instead of crashing

# Catch MULTIPLE specific errors
print("\n2. Multiple exception handlers:")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("   → Error: Cannot divide by zero")
        return None
    except TypeError:
        print("   → Error: Both values must be numbers")
        return None

print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) =", end=" ")
safe_divide(10, 0)
print(f"safe_divide(10, 'x') =", end=" ")
safe_divide(10, "x")

# else - runs only if NO error occurred
# finally - ALWAYS runs (error or not) - good for cleanup
print("\n3. Using else and finally:")
def read_number_from_input(text):
    try:
        number = int(text)
    except ValueError:
        print(f"   → '{text}' is not a valid number, using 0")
        number = 0
    else:
        print(f"   ✓ Successfully read: {number}")  # only if no error
    finally:
        print("   → Processing complete")
    return number

read_number_from_input("42")
read_number_from_input("hello")

# ============================================
# SECTION 8: REAL-WORLD EXAMPLE - MESSY DATA
# ============================================

print("\n=== HANDLING MESSY DATA ===")

# Messy data with problems
with open("messy_sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["rep", "sales", "region"])
    writer.writerow(["Arun",  "85000", "South"])
    writer.writerow(["Priya", "N/A",   "North"])  # bad value
    writer.writerow(["Ravi",  "71000", "East"])
    writer.writerow(["Divya", "",      "West"])   # empty value
    writer.writerow(["Karthik","93000", "South"])

# Robust reader — skips bad rows, reports them
good_rows = []
bad_rows = []

with open("messy_sales.csv", "r") as f:
    for i, row in enumerate(csv.DictReader(f), start=2):
        try:
            sales = int(row["sales"])   # will fail on "N/A" and ""
            if sales <= 0:
                raise ValueError("Sales must be positive")
            good_rows.append({"rep": row["rep"], "sales": sales})
        except ValueError as e:
            bad_rows.append(f"Row {i}: {row['rep']} — {e}")

print(f"Processed: {len(good_rows)} good, {len(bad_rows)} skipped")
print(f"Total sales: {sum(r['sales'] for r in good_rows):,}")
print("Skipped rows:")
for bad in bad_rows:
    print(f"   {bad}")

# OUTPUT:
# Processed: 3 good, 2 skipped
# Total sales: 249,000
# Skipped rows:
#    Row 3: Priya — invalid literal for int() with base 10: 'N/A'
#    Row 5: Divya — invalid literal for int() with base 10: ''

# ============================================
# SECTION 9: COMPREHENSIVE CALCULATOR WITH ERROR HANDLING
# ============================================

print("\n=== SAFE CALCULATOR ===")

def safe_calculate(a, b, operation):
    try:
        if operation == "+":  
            return a + b
        elif operation == "-": 
            return a - b
        elif operation == "*": 
            return a * b
        elif operation == "/":
            if b == 0: 
                raise ZeroDivisionError
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Inputs must be numbers"
    except ValueError as e:
        return f"Error: {e}"

print(f"10 + 5 = {safe_calculate(10, 5, '+')}")      # 15
print(f"10 - 3 = {safe_calculate(10, 3, '-')}")      # 7
print(f"10 * 2 = {safe_calculate(10, 2, '*')}")      # 20
print(f"10 / 2 = {safe_calculate(10, 2, '/')}")      # 5.0
print(f"10 / 0 = {safe_calculate(10, 0, '/')}")      # Error: divide by zero
print(f"'x' + 5 = {safe_calculate('x', 5, '+')}")    # Error: Inputs must be numbers
print(f"5 % 3 = {safe_calculate(5, 3, '%')}")        # Error: Unknown operation: %

# ============================================
# SECTION 10: BEST PRACTICES SUMMARY
# ============================================

print("\n" + "="*50)
print("BEST PRACTICES SUMMARY")
print("="*50)

best_practices = """
1. FILE OPERATIONS:
   ✓ ALWAYS use 'with open()' instead of open/close
   ✓ This ensures files are closed even if errors occur
   
2. READING CSV FILES:
   ✓ Use csv.DictReader for cleaner code (row as dict)
   ✓ Remember: CSV values are always strings initially
   ✓ Convert to int/float when needed
   
3. ERROR HANDLING:
   ✓ Use try/except to prevent crashes
   ✓ Catch specific exceptions, not generic Exception
   ✓ Use else for code that runs only if no error
   ✓ Use finally for cleanup (closing files, etc)
   
4. DATA VALIDATION:
   ✓ Validate data before using it
   ✓ Handle missing/invalid values gracefully
   ✓ Log/report bad data for review
   
5. FILE MODES:
   "r" = read only       | Must exist
   "w" = write only      | Creates/overwrites
   "a" = append          | Adds to end
   "r+" = read + write   | Must exist
"""

print(best_practices)
