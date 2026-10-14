
from datetime import date
from decimal import Decimal

from rekening import Rekening


# Maak een nieuwe spaarrekening aan
rekening = Rekening("15000")

# De basisrente voor spaarders
basisrente = Decimal("1.8")

# Datum waarop we rente berekenen
datum = date(2025, 1, 1)

# Bereken de rente voor één dag
rekening.bereken_rente(datum, basisrente)

# Toon de gegevens
print("SVI Bank - Spaarrekening")
print("Saldo: €", rekening.toon_saldo())

print(
    "Opgebouwde rente: €",
    round(rekening.toon_opgebouwde_rente(), 2)
)
