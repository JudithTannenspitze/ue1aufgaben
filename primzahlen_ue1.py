"""Mit Ausnahme der Zahl 2 sind alle Primzahlen ungerade, denn alle größeren geraden 
Zahlen lassen sich außer durch sich selbst und 1 auch noch (mindestens) durch 2 teilen"""
""" Von 2 bis n/2 testen, da ein Teil größer als n/2 nie eine ganze zahl ergeben kann"""

def primzahl_pruefen(zahlp):
    for zahl in range(2,zahlp,1):
        if zahlp%zahl ==0:
            return str(zahlp) + ": Zahl ist keine Primzahl"
    return str(zahlp) + ": Zahl ist eine Primzahl"


print(primzahl_pruefen(8))
print(primzahl_pruefen(9))
print(primzahl_pruefen(10))
print(primzahl_pruefen(240))
print(primzahl_pruefen(1024))

print("19: " + str(primzahl_pruefen(19)))
print("23: " + str(primzahl_pruefen(23)))
print("47: " + str(primzahl_pruefen(47)))
print("67: " + str(primzahl_pruefen(67)))
print("89: " + str(primzahl_pruefen(89)))