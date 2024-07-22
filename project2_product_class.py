###########################################################
#                                                         #
#  Author: Elisa Wu                                       #
#  Date: 31/05/2023                                       #
#  Purpose: A simple Python Product Class                 #
#                                                         #
###########################################################

# As part of the prototype solution, create a Product class
# to store and manage the following information about a product.

class Product:
    
    def __init__(self, productCode, productName, sellingPrice, productQuantity):
        self.productCode = productCode
        self.productName = productName
        self.sellingPrice = sellingPrice
        self.productQuantity = productQuantity
        
    def displayDetails(self):
        """
        Description: This function will display the details of the product
        
        Params: self
        Return: NA
        
        """
        print("The Product Code is:",self.productCode)
        print("The Product Name is:",self.productName)
        print("Price per item is: $",self.sellingPrice)
        print("The Product Quantity is:",self.productQuantity)
        
    def applyDiscount(self, discount):
        """
        Description: This function will receive discount value as input and return the discounted price.
        
        Params: self, discount
        Return: NA
        """
        discountedPrice = self.sellingPrice - (self.sellingPrice * discount)
        return discountedPrice
    
    def getTotalPrice(self, discount):
        """
        Description: Calculates the total price
        
        Params: self, discount
        Return:
        """
        discountedPrice = self.applyDiscount(discount)
        totalPrice = self.productQuantity * discountedPrice
        return totalPrice


############################
#                          #          
# Main Program Begins here #
#                          #
############################

# Create an instance of the Product class
product = Product("E001", "Chocolate", 5.00, 50)

discountedPrice = product.applyDiscount(0.8)

product.displayDetails()
print("The discounted price is: $",discountedPrice)

totalPrice = product.getTotalPrice(0.8)
print("The total price is: $",totalPrice)
    
    

