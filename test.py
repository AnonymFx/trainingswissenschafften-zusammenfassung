#!/usr/bin/python3

from re import sub

inp = """
•
Varianten
– allgemein vs. speziell
– aktiv vs. passiv
– physisch vs. mental
•
Primäreffekte
– Anregung Herz-Kreislaufsystem
(Kerntemperatur, Atmung, Puls, Blutdruck)
– Durchblutung Muskultur
– Flüssigkeitsregulation Knorpelgewebe
•
Gewünschte Wirkung
– Physische Leistungssteigerung
(Sauerstoffversorgung, Erregbarkeit,
Muskelviskosität, ...)
– Verletzungsprophylaxe
– Psychische Aspekte
"""

inp = inp.replace('\n', '')
print(inp)

inp = sub(r'•([\w ]*)–', r'\n\\item \1:', inp)


# inp = inp.replace('•', '\n\item ')
inp = inp.replace('–', ',')

print(inp)
