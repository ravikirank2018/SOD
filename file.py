import math

# Read coefficients from a file
with open("coefficients.txt", "r") as file:
    data = file.readline().strip()
    a, b, c = map(float, data.split())

# Calculate discriminant
discriminant = b**2 - 4*a*c

# Check for real roots
if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots are: {root1} and {root2}")
else:
    print("No real roots.")