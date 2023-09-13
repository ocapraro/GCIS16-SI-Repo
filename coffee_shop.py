"""
Coffee price calculation plus tax adds free milk!

author: Oscar Capraro
"""


def order_coffee():
  """
  This function requires user to make 3 inputs of different types of coffee and calculates total cost plus tax.
  """
  regular_price = 3
  iced_price = 3.5
  espresso_price = 4.5
  regular = int(input("How many regular coffees would you like? "))
  iced = int(input("How many iced coffees would you like? "))
  espresso = int(input("How many espresso coffees would you like? "))

  tax = 0.06
  no_tax = (regular*regular_price+iced*iced_price+espresso*espresso_price)
  
  # The total is the total plus the total times the tax
  total = no_tax + (no_tax*tax)

  print("Your total is:",total)

order_coffee()