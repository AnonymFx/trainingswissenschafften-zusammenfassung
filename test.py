#!/usr/bin/python3

from re import sub

inp = """
•
Kulturell-erzieherische Funktion
– Fair-Play, Aneignung von
Charaktereigenschaften
•
Soziale Funktion
– Ausbildung von Zusammengehörigkeitsgefühl
•
Kommerzielle Funktion
– Profisport, materieller Gewinn
•
Unterhaltungsfunktion
– Medienunternehmen
•
Politische Funktion
– Z.B. Symbolcharakter für die
Leistungsfähigkeit einer Nation
"""

inp = inp.replace('\n', '')
print(inp)

# inp = sub(r'•([\w ]*)–', r'\n\\item \1:', inp)


inp = inp.replace('•', '\n\item ')
inp = inp.replace('–', ': ')

print(inp)
