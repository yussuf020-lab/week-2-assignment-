# Step 1 & 2: Get user input and convert strings to numerical types
price = float(input("Enter the price of one item ($): "))
quantity = int(input("Enter the quantity you want to purchase: "))

# Step 3: Calculate the total cost
total = price * quantity

# Step 4: Print a friendly summary using an f-string
# :.2f formats the floating-point numbers to always display 2 decimal places
print(f"\nSummary: {quantity} items at ${price:.2f} each = ${total:.2f}")