###########################################################
#                                                         #
#  Author: Elisa Wu                                       #
#  Date: 31/05/2023                                       #
#  Purpose: A simple Product Manage System                #
#                                                         #
###########################################################



# Store a few products in the product lists to start with

productIds = [1001, 1002, 1003]
productNames = ["Black Chocolate", "Bread", "Ice Cream"]
productPrices = [5.00, 3.00, 7.00]
productQuantities = [40, 50, 45]
productCategories = ["Chocolate", "Baked Food", "Frozen Food"]

def addProduct():

    """
    Description: Function to allow user to add products to the product list.
    
    Params: NA
    Return: NA
    """
    
    while True:
 
        productId = int(input("Please enter the Product ID: "))
        
        # Get Product details from the user
        
        # Check if product id already exists or not.
        while productId in productIds:
            productId = int(input("This Product ID already exsits, please enter another Product ID: "))
            
        productName = input("Please enter the Product Name: ")
        productCategory = input("Please enter the Product Category: ")
        productPrice = float(input("Please enter the Product Price: "))
        
        
        # Check if the quantity is in between 10 to 50
        while True:
            productQuantity = int(input("Please enter the Product Quantity in between 10 to 50: "))
            if productQuantity in range(10, 51):
                break

        # Add the Product details to the Product List              
        productIds.append(productId)
        productNames.append(productName)
        productCategories.append(productCategory)
        productPrices.append(productPrice)
        productQuantities.append(productQuantity)
        
        choice = input("Do you want to add more Products (Yes/No): ")
        
        if choice.lower() == "no":
            break


def checkProduct(productId):
 
    """
        Description: Function to check whether the given productId exists or not
    
        Params: productId (Integer)
        Return: True or False
    
    """
    
    if productId in productIds:
        return True
    else:
        return False

 
def searchProduct(productId):
    
    """
        Description: Function which calls checkProduct() function to check whether the given productId exists or not
                     and prints the Product Details if it exists.
    
        Params: productId (Integer)
        Return: NA
    
    """
    
    # Check if the Product Id is in the Product List or not.
    while checkProduct(productId) is False:
        print("This Product doesn't exist in the Product List.")
        productId = int(input("Please enter the correct Product Id to search: "))
    
    # Get the Product Id Index and print the Product Details.
    index = productIds.index(productId)
    
    print("\n")
    print("Product Details:")
    print("----------------------------")
    print("Product Id:", productId)
    print("Product Name:", productNames[index])
    print("Product Category:", productCategories[index])
    print("Product Price:", productPrices[index])
    print("Product Quantity:", productQuantities[index])
    print("\n")
        
def updateProduct(productId):
    
    """
    Description: Updates the Product Details if if it exists exists.
                 Calls searchProduct() function
    
    Params: productId(Integer)
    Return: NA

    """
 
    # Call searchProduct() which checks and prints Product details if it exists.
    # searchProduct() displays an error message until a correct Product Id is entered.
    searchProduct(productId)

    index = productIds.index(productId)
    
    decision = input("Please confirm if this is the Product you want to update. (Yes/No): ")
    
    while True:
        if decision.lower() == "yes":
            
            while True:
                option = int(input("""

Product Properties to update:
1. Product Name
2. Product Price
3. Product Quantity
4. Product Category
                
Please choose the property you want to update. Enter 1, 2, 3, 4 or enter 0 to stop updating: """))
                
                if option == 0:
                    # To break the outer while loop
                    decision = "No"
                    break
                elif option == 1:
                    productNames[index] = input("Please enter a new Product Name: ")
                elif option == 2:
                    productPrices[index] = float(input("Please enter a new Product Price: "))
                elif option == 3:
                    newQuantity = int(input("Please enter a new Product Quantity: "))
                    while newQuantity not in range(10, 51):
                        print("The Quantity should be in between 10 and 50.")
                        newQuantity = int(input("Please enter a new Product Quantity: "))
                    productQuantities[index] = newQuantity
                elif option == 4:
                    productCategories[index] = input("Please enter a new Product Category: ")
                else:
                    option = int("Invalid choice. Please enter 1, 2, 3, 4 or enter 0 to stop updating: ")
        elif decision.lower() == "no":
            break
        else:
            decision = input("Invalid choice. Please enter Yes or No: ")
            
def buyProduct(productId, productQuantity):
    
    """
    Description: Function to purchase the products.
                 It calls searchProduct() to check a product and display the details.
                 It calculates the Total Price with GST and applies discount.
                 Updates the Product quantity after successful purchase.
    
    Params: productId (Integer), productQuantity(Integer)
    Return: NA
    """

    # Check if Product Id exists by using searchProduct() function before proceeding further.
    searchProduct(productId)
    
    decision = input("Please confirm if this is the Product you would like to buy (Yes/No): ")
    
    while True:
        if decision.lower() == "yes":
            index = productIds.index(productId)
            
            if productQuantity <= productQuantities[index]:
                totalPriceExcludingGST = productPrices[index] * productQuantity
                gstAmount = totalPriceExcludingGST * 0.15
                totalPriceIncludingGST = totalPriceExcludingGST + gstAmount
                    
                if 10 <= productQuantity < 20:
                    discount = totalPriceIncludingGST * 0.1
                    finalPriceWithDiscount = totalPriceIncludingGST - discount
                elif 20 <= productQuantity < 30:
                    discount = totalPriceIncludingGST * 0.2
                    finalPriceWithDiscount = totalPriceIncludingGST - discount
                elif productQuantity >= 30:
                    discount = totalPriceIncludingGST * 0.3
                    finalPriceWithDiscount = totalPriceIncludingGST - discount
                else:
                    discount = 0
                    finalPriceWithDiscount = totalPriceIncludingGST
                    #No discount is given for quantities below 10
                
                print("\n---Purchase Order Details---\n")
                print("Product Purchased: {}".format(productNames[index]))
                print("Product Price: $%.2f" %productPrices[index])
                print("Quantity of Products: {}".format(productQuantity))
                print("\n")
                print("Total Price (Incl GST): $%.2f" %totalPriceIncludingGST)
                print("Discount applied: $%.2f" %discount)
                print("Total Price with Discount: $%.2f" %finalPriceWithDiscount)
                
                # Update the Product Quantity
                productQuantities[index] -= productQuantity
                
                print("\nPurchase successful.\n")
                
            else:
                print("There are only {} of the Product '{}' available for sale.".format(productQuantities[index], productNames[index]))
                choice = input("Do you want to enter a new Product Quantity? (Yes/No): ")
                if choice.lower() == "yes":
                    newQuantity = int(input("Please enter the Quantity of this Product you want to purchase: "))
                    buyProduct(productId, newQuantity)
                else:
                    print("Sorry! Purchase failed.")
                    break
            
            break

        elif decision.lower() == "no":
            productId = int(input("Please enter the Product Id that you want to buy: "))
            buyProduct(productId, productQuantity)

        else:
            decision = input("Please choose 'Yes' or 'No': ")


############################
#                          #          
# Main Program Begins here #
#                          #
############################

menuOption = 0
while menuOption <= 5:
    print("\n-----Welcome to Product Management System-----\n")
    print("	1. Add New Product")
    print("	2. Search Product")
    print("	3. Update Product Details")
    print("	4. Buy Product")
    print("	5. Exit")
    print("\n")
    
    menuOption = int(input("Please select from the menu either 1,2,3,4 or 5: "))
    
    if menuOption == 1:
        addProduct()
        
    elif menuOption == 2:
        while True:
            productId = int(input("Please enter the Product ID: "))
            searchProduct(productId)
            choice = input("Do you want to search more Products (Yes/No): ")
            if choice.lower() != "yes":
                break
            
    elif menuOption == 3:
        productId = int(input("Please enter the Product Id: "))
        while checkProduct(productId) is False:
            print("This Product doesn't exist in the Product list.")
            productId = int(input("Please enter the correct Product Id: "))
        updateProduct(productId)
        
    elif menuOption == 4:
        productId = int(input("Please enter the Product Id: "))
        while checkProduct(productId) is False:
            print("This Product doesn't exist in the Product List.")
            productId = int(input("Please enter the correct Product Id: "))
        
        while True:
            productQuantity = int(input("Please enter the Quantity of Products you want to purchase: " ))
            if productQuantity <= 0:
                print("Product Quanity should be > 0.")
            else:
                break
                
        buyProduct(productId, productQuantity)
        
    elif menuOption == 5:
        print("\nThank you for using our Product Management System!\n")
        break
    else:
        menuOption = int(input("Please enter 1,2,3, 4 or 5: "))
