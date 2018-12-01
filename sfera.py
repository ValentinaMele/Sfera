import math
def volumeSfera (r):
     return 4./3. * math.pi * r**3


r=input("Inserisci il raggio")
r=int(r)
risultato=volumeSfera(r)


print(risultato)