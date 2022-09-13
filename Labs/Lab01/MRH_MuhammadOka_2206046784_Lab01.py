######################################
# Lab 01 - Programming Foundations 1 #
#            Muhammad Oka            #
#             2206046784             #
######################################

# Declare rates
hourly_rate = 300
accommodation_rate = 50
usd_to_idr = 14888

# Print title
print("-------------------------------------")
print("| Farel Prayoga's Salary Calculator |")
print("-------------------------------------\n")

# Ask for input
hours = input("How many hours did Farel show? ")
days = input("How many days did Farel stay? ")

# Calculate show salary, accommodation total price, and salary before tax
show_salary = hourly_rate * float(hours)
accommodation_total_price = accommodation_rate * int(days)
salary_before_tax = show_salary - accommodation_total_price

# Print the salary and salary after accommodation
print("")
print(f"Salary = USD {int(show_salary)}")
print(f"After accommodation = USD {int(accommodation_total_price)}")
print("")

# Calculate salary after tax and convert to IDR
salary_after_tax = salary_before_tax - (salary_before_tax * 0.1)
salary_to_idr = salary_after_tax * usd_to_idr

# Format IDR to seperate thousands
salary_idr_formatted = f"{int(salary_to_idr):,}".replace(",", ".")

# Print net salary
print(f"Farel's net salary after tax and accommodation is USD {int(salary_after_tax)}")
print(f"After conversion, Farel's net salary is IDR {salary_idr_formatted}")