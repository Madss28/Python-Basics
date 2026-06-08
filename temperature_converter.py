"""
TEMPERATURE CONVERTER
A professional-grade conversion tool with multiple functions.
Demonstrates: functions, parameters, return values, docstrings, input validation
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    
    Example:
        >>> celsius_to_fahrenheit(37)
        98.6
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Kelvin
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    
    Args:
        kelvin (float): Temperature in Kelvin
    
    Returns:
        float: Temperature in Celsius
    """
    return kelvin - 273.15


def validate_temperature(value, scale):
    """
    Validate that temperature is physically possible.
    
    Args:
        value (float): Temperature value
        scale (str): 'C', 'F', or 'K'
    
    Returns:
        bool: True if valid, False otherwise
    """
    if scale.upper() == 'K' and value < 0:
        return False
    elif scale.upper() == 'C' and value < -273.15:
        return False
    elif scale.upper() == 'F' and value < -459.67:
        return False
    return True


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("        PROFESSIONAL TEMPERATURE CONVERTER")
    print("=" * 50)
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Exit")
    print("-" * 50)


def main():
    """Main program loop."""
    print("\nWelcome to the Professional Temperature Converter")
    print("This tool converts between Celsius, Fahrenheit, and Kelvin.")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            if validate_temperature(celsius, 'C'):
                result = celsius_to_fahrenheit(celsius)
                print(f"\n✅ {celsius}°C = {result:.2f}°F")
            else:
                print("\n❌ Error: Temperature below absolute zero!")
        
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            if validate_temperature(fahrenheit, 'F'):
                result = fahrenheit_to_celsius(fahrenheit)
                print(f"\n✅ {fahrenheit}°F = {result:.2f}°C")
            else:
                print("\n❌ Error: Temperature below absolute zero!")
        
        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            if validate_temperature(celsius, 'C'):
                result = celsius_to_kelvin(celsius)
                print(f"\n✅ {celsius}°C = {result:.2f}K")
            else:
                print("\n❌ Error: Temperature below absolute zero!")
        
        elif choice == "4":
            kelvin = float(input("Enter temperature in Kelvin: "))
            if validate_temperature(kelvin, 'K'):
                result = kelvin_to_celsius(kelvin)
                print(f"\n✅ {kelvin}K = {result:.2f}°C")
            else:
                print("\n❌ Error: Temperature below absolute zero!")
        
        elif choice == "5":
            print("\n👋 Thank you for using the Temperature Converter!")
            print("GitHub: github.com/Madss28")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
