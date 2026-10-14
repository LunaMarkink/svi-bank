
from datetime import date
from decimal import Decimal

from rente import bereken_dagrente

# Gegevens van een voorbeeldrekening
saldo = Decimal("10000")
rentepercentage = Decimal("1.8")
datum = date(2025, 1, 1)

# Bereken de dagrente
dagrente = bereken_dagrente(
    saldo,
    rentepercentage,
    datum
)

# Toon de uitkomst
print("SVI Bank - Renteberekening")
print("Saldo: €", saldo)
print("Rentepercentage:", rentepercentage, "%")
print("Dagrente: €", round(dagrente, 2))
