
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


def bepaal_renteaanpassing(saldo):
    """
    Bepaalt de renteaanpassing op basis van de saldoklasse.

    saldo: het huidige spaarsaldo van de klant
    """

    if saldo < Decimal("0"):
        raise ValueError("Saldo mag niet negatief zijn.")

    if saldo <= Decimal("10000"):
        return Decimal("-0.25")

    elif saldo <= Decimal("25000"):
        return Decimal("0")

    elif saldo <= Decimal("50000"):
        return Decimal("-0.15")

    elif saldo <= Decimal("100000"):
        return Decimal("-0.25")

    elif saldo <= Decimal("1000000"):
        return Decimal("-0.50")

    else:
        return None


def bepaal_rentepercentage(saldo, basisrente):
    """
    Berekent het jaarlijkse rentepercentage
    op basis van de saldoklasse.
    """

    aanpassing = bepaal_renteaanpassing(saldo)

    # Boven 1 miljoen ontvangt klant geen rente
    if aanpassing is None:
        return Decimal("0")

    return basisrente + aanpassing



def is_laatste_dag_kwartaal(datum):
    """Controleert of een datum de laatste dag van een kwartaal is."""

    kwartaal_einddatums = [
        (3, 31),
        (6, 30),
        (9, 30),
        (12, 31)
    ]

    return (datum.month, datum.day) in kwartaal_einddatums
