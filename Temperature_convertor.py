# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_fahrenheit_and_kelvin(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_celsius_and_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_and_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main program
def main():
    # Prompt the user to input the temperature value and unit
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of temperature (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    # Convert and display the results
    if unit == "celsius":
        fahrenheit, kelvin = celsius_to_fahrenheit_and_kelvin(temp)
        print(f"{temp}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit and {kelvin:.2f} Kelvin.")
    elif unit == "fahrenheit":
        celsius, kelvin = fahrenheit_to_celsius_and_kelvin(temp)
        print(f"{temp}° Fahrenheit is equal to {celsius:.2f}° Celsius and {kelvin:.2f} Kelvin.")
    elif unit == "kelvin":
        celsius, fahrenheit = kelvin_to_celsius_and_fahrenheit(temp)
        print(f"{temp} Kelvin is equal to {celsius:.2f}° Celsius and {fahrenheit:.2f}° Fahrenheit.")
    else:
        print("Invalid unit entered. Please enter Celsius, Fahrenheit, or Kelvin.")

# Run the main program
if __name__ == "__main__":
    main()
