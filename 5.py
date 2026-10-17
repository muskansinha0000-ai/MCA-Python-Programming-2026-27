p1 = float(input("Enter price of Product 1: "))
q1 = int(input("Enter quantity of Product 1: "))

p2 = float(input("Enter price of Product 2: "))
q2 = int(input("Enter quantity of Product 2: "))

p3 = float(input("Enter price of Product 3: "))
q3 = int(input("Enter quantity of Product 3: "))

subtotal = (p1 * q1) + (p2 * q2) + (p3 * q3)

discount = subtotal * 0.10
amount_after_discount = subtotal - discount

gst = amount_after_discount * 0.18
final_amount = amount_after_discount + gst

print("Subtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Payable Amount =", final_amount)