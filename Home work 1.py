'''
Calculate 530 divided by 7 and give the answer
with up to 2 decimals.
'''
x=530
y=7
z=x/y
print(round(z, 2))
    
'''
Let us use the input function. Ask the name of
a product and ask also the price of the product. For example,
if you gave ‘potatoes’ as a product and 2.35 as a price,
Python should print: The price of the potatoes is 2.35 €
'''
product_name=input("What is the product name? ")
price=float(input("What is the product price? "))
print("The price of the", product_name, "is", price, "€")
'''
Python asks your first name and then your last name.
If you gave Charlie and Brown, the following text should be printed:
Your name is Charlie Brown.
'''
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
print("Your name is", first_name, last_name)
'''
We have a formula to calculate the interest r, if the capital k,
interest percentage p and time t are known. The formula is r=(k p t)/100.
Write the formula with Python, when t = 1, capital is 30000 and p = 2.3%
'''
t=1
p=2.3
k=30000
r=(k*p*t)/100
print(r)
