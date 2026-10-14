
from datetime import date
from decimal import Decimal

from rente import bereken_dagrente, bepaal_rentepercentage

# Voorbeeldgegevens van een klant
saldo = Decimal("15000")
basisrente = Decimal("1.8")
datum = date(2025, 1, 1)

# Bepaal het rentepercentage
rentepercentage = bepaal_rentepercentage(
    saldo,
    basisrente
)

# Bereken de rente voor één dag
dagrente = bereken_dagrente(
    saldo,
    rentepercentage,
    datum
)

print("SVI Bank - Renteberekening")
print("Saldo: €", saldo)
print("Rentepercentage:", rentepercentage, "%")
print("Dagrente: €", round(dagrente, 2))
