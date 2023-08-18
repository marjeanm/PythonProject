#descriptions 
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

"""
stylish_settee_description = """ Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
luxurious_lamp_description = """ Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

#price
lovely_love_seat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

#tax 
sales_tax = .088

#customer purchase
#customer one
customer_one_total = 0
customer_one_itemization =""


# tax
customer_one_tax = customer_one_total * sales_tax

# add price to totals
customer_one_total = lovely_love_seat_price + luxurious_lamp_price + customer_one_tax

# description of the items 
customer_one_itemization =lovely_loveseat_description + luxurious_lamp_description


#receipt 
print("Customer One Items : " + customer_one_itemization )
print("Customer One Total: " + str(customer_one_total))