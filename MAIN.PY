# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_conversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_conversion(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_conversion(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main function to take user input and perform conversions
def temperature_conversion():
    print("Welcome to Temperature Conversion Program")
    print("Choose the temperature unit you want to convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit, kelvin = celsius_conversion(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
        print(f"{celsius}°C = {kelvin:.2f}K")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius, kelvin = fahrenheit_conversion(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
        print(f"{fahrenheit}°F = {kelvin:.2f}K")

    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius, fahrenheit = kelvin_conversion(kelvin)
        print(f"{kelvin}K = {celsius:.2f}°C")
        print(f"{kelvin}K = {fahrenheit:.2f}°F")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Run the temperature conversion program
if __name__ == "__main__":
    temperature_conversion()
