# OTT Login program
'''
username = input("Enter username > ")
password = input("Enter password > ")
age = int(input("Enter your age > "))
plan = input("Enter your plan (Basic  / premium  /  Vip > ")

if username == "muddu" and password == "1021":
    print(" < Login successful >")
else:
    print("wrong credentials, access denied")
    exit()

if plan not in ["Basic", "Premium", "VIP"]:
    print("Invalid plan. Choose Basic, premium or Vip")

if age < 13:
    category = "Kids"
elif age < 18:
    category = "Teen"
else:
    category = "Adult"

hd = "yes" if plan == "premium" or plan == "Vip" else "no"

if plan=="Basic":
    screens = 1
    price = 99
elif plan=="premium":
    screens = 3
    price = 299
elif plan=="Vip":
    screens = 5
    price = 499

print(f"Welcome {username}")

print(f"plan: {plan.upper()} | {price}/month")
print(f"screens: {screens} | HD: {hd}")
print(f"Content category: {category}")''''



employee_name = input("Enter employee name ")
employee_age = int(input("Enter employee age "))
current_ctc = float(input("Enter current ctc "))
referral = bool(input("Enter referral status "))
offered_ctc = current_ctc * 1.5


print("Employee details::")

print(f"Employee name is {employee_name}")
print(f"Employee age is {employee_age}")
print(f"Employee current ctc is {current_ctc}")
print(f"Employee offered ctc is {offered_ctc}")
print(f"Referral is {referral}")


































