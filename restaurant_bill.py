#Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#define and set variables from user input (casted to a float)

meal = float(input("how much is the meal?"))
tax = float(input("what is the sales tax (percentage)?"))
tip = float(input("how much of a tip (percentage)?"))               

#calculate and add tax
tax_amount = (meal * tax) / 100 #calculate the tax
total_bill = meal + tax_amount #add tax amount to the final bill

#calculate and add tip
tip_amount = (total_bill * tip) / 100 #calculate the tip
total_bill = total_bill + tip_amount #add tip amount to final bill

#round the total to 2 decimal places
total_bill = round(total_bill, 2) #round the total amount to 2 decimal places

#print the final amount
print("the tax of your bill is $", tax_amount)
print("the tip of your bill is $", tip_amount)
print("the total bill is $", total_bill)