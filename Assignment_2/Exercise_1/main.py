import math
import rec_area
import sq_area
import cir_area
pi = 3.14

print("Enter 1 : Area of Rectangle")
print("Enter 2 : Area of square")
print("Enter 3 : Area of Circle")

option = int(input("Choose the Option (1 to 3) :"))

if(option == 1):
    len = int(input("Enter the Length :"))
    br = int(input("Enter the Breadth :"))
    rec_area.rec_area(len,br)
elif(option == 2):
    side = int(input("Enter the side :"))
    sq_area.sq_area(side)
elif(option == 3):
    radius = int(input("Enter the radius :"))
    cir_area.cir_area(radius)
else:
    print("Invalid option selected. Try Again.")

