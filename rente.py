from datetime import date
from decimal import Decimal


def is_schrikkeljaar(jaar):
    """Controleert of een jaar een schrikkeljaar is."""
    return jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0)


def aantal_dagen_in_jaar(datum):
    """Geeft het aantal dagen van het opgegeven jaar terug."""
    if is_schrikkeljaar(datum.year):
        return 366

    return 365


def bereken_dagrente(saldo, rentepercentage, datum):
    """
    Berekent de rente voor één dag.

    saldo: het huidige saldo van de klant
    rentepercentage: de jaarlijkse rente in procenten
    datum: de datum waarop de rente wordt berekend
    """

    # Bepaal hoeveel dagen het jaar heeft
    dagen = aantal_dagen_in_jaar(datum)

    # Berekent de rente over één dag
    dagrente = (
        saldo * rentepercentage
        / Decimal("100")
        / Decimal(dagen)
    )

    return dagrente
