print("\n PROGRAM KONVERSI TEMPERATUR \n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah ",celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",reamur, "Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

#Kelvin
kelvin = celcius+273
print("Suhu dalam Kelvin adalah ",kelvin, "Kelvin")
