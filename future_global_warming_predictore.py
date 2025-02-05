running = True
temp_per_yr = 0.20
temp = 13.9
Input = float(input("Enter year here "))
future_temp = temp_per_yr * (Input - 2024)
while running:
    if Input >= 2024:
        future_temp += temp
        running = False
if future_temp > 18:
    print(f"(not suitable): {future_temp}")
else:
    print(f"its okay: {future_temp}")

