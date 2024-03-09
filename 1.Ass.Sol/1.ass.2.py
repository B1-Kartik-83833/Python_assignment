#2] Write a Python Program to Convert Celsius To Fahrenheit vice versa.
# fahrenheit = (celsius * 1.8) + 32
faren=lambda cel:(cel * 1.8)+32
cel=int(input("Enter the celcius: "))
print(f"Celius to farenheit= {faren(cel)}")
cel=lambda faren:(faren-32)*0.55
faren=int(input("Enter the farenheit: "))
print(f"Farenheit to celcius= {cel(faren)}")
