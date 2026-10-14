
from datetime import date
from rente import aantal_dagen_in_jaar

# De startdatum van het SVI-banksysteem
startdatum = date(2025, 1, 1)

# Bepaal hoeveel dagen het jaar heeft
dagen = aantal_dagen_in_jaar(startdatum)

print("SVI Bank - Renteberekening")
print("Startdatum:", startdatum)
print("Aantal dagen in het jaar:", dagen)
