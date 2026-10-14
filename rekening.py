
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
        self.uitgekeerde_kwartalen = set()

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
        """Keert rente maximaal één keer per kwartaal uit."""

        from rente import is_laatste_dag_kwartaal

        if not is_laatste_dag_kwartaal(datum):
            return Decimal("0")

        # Bepaal het jaar en kwartaal
        kwartaal = (datum.year, (datum.month - 1) // 3 + 1)

        # Controleer of dit kwartaal al is uitgekeerd
        if kwartaal in self.uitgekeerde_kwartalen:
            return Decimal("0")

        # Rond de opgebouwde rente af
        rente_uitkering = self.opgebouwde_rente.quantize(
            Decimal("0.01")
        )

        # Verwerk de uitkering
        self.saldo += rente_uitkering
        self.uitgekeerde_rente += rente_uitkering
        self.opgebouwde_rente = Decimal("0")

        # Onthoud dat dit kwartaal is verwerkt
        self.uitgekeerde_kwartalen.add(kwartaal)

        return rente_uitkering

