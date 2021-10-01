
#Variables
one = "Polo"
two = "T-shirt"
colour = input("What Type Of Colour Of Shirt You Want : ")
Type = input("What Type Of Shirt You Want ? Enter 1 For Polo Or Enter 2 For T-Shirt : ")
quantity = int(input("How Many Shirts You Want : "))
shirt_cost = 9.99
price_without_hst = int(shirt_cost) * int(quantity)
HST = 13
tax = price_without_hst/100
tax1 = tax * HST 
tax2 = price_without_hst + tax1


#Program
print("Welcome To Abby's Merchandise")
print("You Have Selected" , colour , "colour . ")
if Type == "1":
    print("You Have Selected Polo Shirt.")

elif Type == "2":
    print("You Have Selected T-shirt") 

else :
    print("Please Write right option.")
print("The Quantity Of Shirt Will Be :  ")


#Final Outputs
print("Here Is Your Receipt : " )
print("Colour : " , colour)
print("Shirt Type : " , Type)
print("Quantity : " , quantity)
print("Price Without HST : " , "$" , str(price_without_hst))
print("Price With HST : " , "$" , tax2 , "(13% HST)")



