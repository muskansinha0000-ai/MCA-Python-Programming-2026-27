seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)