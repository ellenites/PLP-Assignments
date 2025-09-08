def calculate_discount(price, discount_percent):
   if discount_percent> 0:
      return price-(price*discount_percent/100)
   else:
      return price

price=int(input('Enter the price: '))
discount_percent=int(input('Enter the discount percent: '))
#discount_percent = int(discount_percent) if discount_percent.strip() else 0   # default 0 if empty
calculate_discount(price, discount_percent)
print(calculate_discount(price, discount_percent))