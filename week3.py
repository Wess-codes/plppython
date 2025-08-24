def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final = calculate_discount(original_price, discount)

    if final != original_price:
        print(f"Discount applied! Final price: {final:.2f}")
    else:
        print(f"No discount applied. Final price: {original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
