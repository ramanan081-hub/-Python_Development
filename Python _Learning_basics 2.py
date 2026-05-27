
# File I/O & CSV handling

# METHOD 1: Basic opne /close (you must close manually)

file = open("data.txt","r") # r- read mode
content = file.read()
file.close()    # MUST close - or data stays locked

# METHOD 2: with open()- ALWAYS use this (auto-closes)
with open("data.txt","r") as file:
    content = file.read()

# file is automatically closed when the with block ends
print(content)

# File modes -what the second argument means 
# "r" - read only(file must exist)
# "w" - write (creates new file or overwrtes existing)
# "a" - append (add to end of existing file)
# "r+" - read and write 


# first, create a test file to work with 
#(Run this once to create the file)
with open("employees.txt","w") as f:
    f.write("Arun,Sales,55000\n")
    f.write("Priya,Analyst,75000\n")
    f.write("Ravi,IT,68000\n")
    f.write("Divya,Sales,52000\n")

# newline character(like pressing Enter in a text file)

#READ METHOD1: read() -entire file as one big string
with open("employees.txt","r") as f:
    all_text = f.read()
print(all_text)
print(type(all_text))

#READ METHODE2: readline() - list of lines(each line = one string)
with open("employees.txt","r") as f:
    lines = f.readlines()
print(lines)
print(lines[0])
print(lines[0].strip())

#READ METHOD3: iterate line by line - bast for large files
with open("employees.txt","r") as f:
    for line in f:
        clean = line.strip()

        parts = clean.split(",")
        print(f"Name:{parts[0]},Dept:{parts[1]},Salary:{parts[2]}")


# Writing files & reading real CSVs

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

# READING a real CSV file with python's csv module 
import csv

#First create a sample CSV to work with 
with open("sales.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Month","Region","Sales","Target"])
    writer.writerow(["jan","south",85000,80000])
    writer.writerow(["jan","north",62000,70000])
    writer.writerow(["feb","south",91000,80000])
    writer.writerow(["feb","north",77000,70000])

# Reading CSV -DirctReader gives each row as a dictionary 
with open("sales.csv","r") as f:
    reader = csv.DictReader(f)      # header row becomes dict keys
    for row in reader:
        sales = int(row["Sales"])    # remember: CSV values are strings
        target = int(row["Target"])
        met = "✓" if sales >= target else "✗"
        print(f"{row['Month']}|{row['Region']}|{sales:,}[{met}]")

import csv

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
print(f"Total products: {len(products)}")
print(f"Total value: {total_value:,}")
print(f"Most expensive: {priciest['product']} at {priciest['price']:,}")