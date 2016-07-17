#!/usr/bin/python3

from re import sub

inp = """
•
•
•
•
Kontraktion im Rumpf vor Bewegung
(Feed-Forward)
Schutzfunktion für die Wirbelsäule
Biomechanische Vorrausetzung für
Wurf-, Schlag-, Schussbewegungen
Belastungsnormative
–
–
–
–
niedrigen Intensitäten (25%)
recht lange (30s)
statisch und dynamisch
keine Periodisierung, trainingsbegleitend
"""

inp = inp.replace('\n', '')
print(inp)

inp = sub(r'•([\w ]*)–', r'\n\\item \1:', inp)


# inp = inp.replace('•', '\n\item ')
inp = inp.replace('–', ',')

print(inp)
