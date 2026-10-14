
from datetime import date, timedelta
from decimal import Decimal
from rekening import Rekening

# Maak een spaarrekening aan
rekening = Rekening("15000")

# Basisrente voor spaarders
basisrente = Decimal("1.8")

# Eerste kwartaal van 2025
datum = date(2025, 1, 1)
einddatum = date(2025, 3, 31)

# Bereken voor iedere dag de rente
while datum <= einddatum:
    rekening.bereken_rente(datum, basisrente)
    datum += timedelta(days=1)

# Toon het saldo en de opgebouwde rente
print("SVI Bank - Kwartaalrente")
print("Saldo voor uitkering: €", rekening.toon_saldo())
print("Opgebouwde rente: €", round(rekening.toon_opgebouwde_rente(), 2))

# Keer de kwartaalrente uit
uitkering = rekening.keer_kwartaalrente_uit(einddatum)

print("Uitgekeerde rente: €", uitkering)
print("Nieuw saldo: €", rekening.toon_saldo())
