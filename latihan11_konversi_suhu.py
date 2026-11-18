# funsi ubah suhu ke fahrenheit dan kelvin
def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celcius_ke_kelvin(c):
    return c + 273.15
input_suhu = float(input("Masukkan suhu dalam celcius: "))
fahrenheit = celcius_ke_fahrenheit(input_suhu)
kelvin = celcius_ke_kelvin(input_suhu)
print(f"{input_suhu} derajat Celcius = {fahrenheit:.2f} derajat Fahrenheit")
print(f"{input_suhu} derajat Celcius = {kelvin:.2f} derajat Kelvin")