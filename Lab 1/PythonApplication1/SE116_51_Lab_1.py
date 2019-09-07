#cookToCode

#This is a program to determine the selling price of an item
#cost item and set percent upsale

#   -cost, the cost of an item
#   -margin, the percent of the upcharge
#   -selling_price, the final price for the item

cost = 25.40        #<----This is how you initiate a variable | variables need to be initiated before used in the code
margin = 20

#the math for finding the selling price 
selling_price = (1/(1-margin/100))*cost

#printing out the final "selling_price"
print("The final price will be $",selling_price) #<--This is called the print method | the syntax is 'print("")'

#The print function above can also be written   'print(f"The final price will be ${selling_price}")'
