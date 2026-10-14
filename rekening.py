
from datetime import date
from decimal import Decimal

from rente import bereken_dagrente, bepaal_rentepercentage


class Rekening:
    """Beheert het saldo en de rente."""

    def __init__(self, beginsaldo):
        # Het saldo waarmee de rekening begint
        self.saldo = Decimal(str(beginsaldo))

        # De rente die nog niet is uitgekeerd
        self.opgebouwde_rente = Decimal("0")
        self.uitgekeerde_rente = Decimal("0")

    def bereken_rente(self, datum, basisrente):
        """Bereken en bewaar de rente van één dag."""

        # Bepaal het rentepercentage voor deze saldoklasse
        rentepercentage = bepaal_rentepercentage(
            self.saldo,
            basisrente
        )

        # Bereken de rente over het huidige saldo
        dagrente = bereken_dagrente(
            self.saldo,
            rentepercentage,
            datum
        )

        # Bewaar de rente, maar verander het saldo niet
        self.opgebouwde_rente += dagrente

        return dagrente

    def toon_saldo(self):
        """Geef het huidige saldo terug."""
        return self.saldo

    def toon_opgebouwde_rente(self):
        """Geef de opgebouwde rente terug."""
        return self.opgebouwde_rente

    
    def keer_kwartaalrente_uit(self, datum):
        """Keert de opgebouwde rente uit aan het einde van een kwartaal."""

        from rente import is_laatste_dag_kwartaal

        # Controleer of het kwartaal is afgelopen
        if not is_laatste_dag_kwartaal(datum):
            return Decimal("0")

        # Rond de opgebouwde rente af op centen
        rente_uitkering = self.opgebouwde_rente.quantize(
            Decimal("0.01")
        )

        # Voeg de rente toe aan het saldo
        self.saldo += rente_uitkering

        # Bewaar hoeveel rente is uitgekeerd
        self.uitgekeerde_rente += rente_uitkering

        # Zet de opgebouwde rente weer op nul
        self.opgebouwde_rente = Decimal("0")

        return rente_uitkering
