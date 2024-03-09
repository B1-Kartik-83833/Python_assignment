# Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price
# is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for quantities over 50.

unit_price = 5
discount_frequency_30 = 30
discount_frequency_50 = 50
discount_rate_10 = 0.1
discount_rate_15 = 0.15

quantity = int(input("Enter the quantity: "))

total_price = quantity * unit_price

if quantity > discount_frequency_50:
    discount_rate = discount_rate_15
elif quantity > discount_frequency_30:
    discount_rate = discount_rate_10
else:
    discount_rate = 0

discount_amount = total_price * discount_rate

final_price = total_price - discount_amount

print(f"Unit price: Rs {unit_price}")
print(f"Quantity: {quantity}")

if discount_rate > 0:
    print(f"Discount rate: {discount_rate * 100:.1f}%")
    print(f"Discount amount: Rs {discount_amount:.2f}")

print(f"Final price: Rs {final_price:.2f}")




