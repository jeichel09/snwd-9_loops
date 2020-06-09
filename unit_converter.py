print("Das ist ein Meilen-Umrechner")
check = 0
miles = 0
while check == 0:
    km = float(input("Gib eine Km-Länge ein: "))
    miles = km*0.621371
    print(str(km) + " Kilometer entsprechen " + str(miles) + " Meilen.")
    frage = input("Brauchst du noch eine Umrechnung? (J/N) ")
    if frage == "N":
        check = 1
    else:
        continue
print("Danke und Auf Wiedersehen!")