#!/usr/bin/python3

from re import sub

inp = """
• Freiheitsgrade:
Sukzessives Freisetzen, „selective defrosting“
• Gestalt:
flüssige, lockere Bewegung, Kombinationen
• Methodik:
Intensive Rückmeldungen, große Wiederholungszahlen
"""

inp = inp.replace('\n', '')
print(inp)

# inp = sub(r'•([\w ]*)–', r'\n\\item \1:', inp)


inp = inp.replace('•', '\n\item ')
inp = inp.replace('–', ',')

print(inp)
