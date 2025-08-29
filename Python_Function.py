# Week 3 Assignment - Discount Calculator

# Step 1: Define the function
def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if >= 20%"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Step 3: Call the function and display results
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied! The final price is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
