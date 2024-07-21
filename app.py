def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {fahrenheit}°F")