print("Please enter unit to convert To")
unit = input("Enter \"C\" if Celsius or \"F\" Fahrenheit): ").strip().lower()

if unit == "c":
    celcius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celcius * (9 / 5)) + 32
    print(f"{celcius:.1f}°C is equal to {fahrenheit:.1f}°F")
elif unit == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print(f"{fahrenheit:.1f}°F is equal to {celsius:.1f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")