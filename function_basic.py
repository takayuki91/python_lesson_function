# 関数（function）

fahrenheit = 72


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)