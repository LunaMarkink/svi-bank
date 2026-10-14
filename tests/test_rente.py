from decimal import Decimal
from rente import bereken_dagrente
from datetime import date
from rente import is_schrikkeljaar, aantal_dagen_in_jaar


def test_schrikkeljaar():
    """Controleert of een schrikkeljaar goed wordt herkend."""
    assert is_schrikkeljaar(2024) == True


def test_geen_schrikkeljaar():
    """Controleert of een normaal jaar goed wordt herkend."""
    assert is_schrikkeljaar(2025) == False


def test_aantal_dagen_normaal_jaar():
    """Controleert of een normaal jaar 365 dagen heeft."""
    datum = date(2025, 1, 1)

    assert aantal_dagen_in_jaar(datum) == 365


def test_aantal_dagen_schrikkeljaar():
    """Controleert of een schrikkeljaar 366 dagen heeft."""
    datum = date(2024, 1, 1)

    assert aantal_dagen_in_jaar(datum) == 366


def test_dagrente_normaal_jaar():
    """Controleert de dagrente in een normaal jaar."""
    saldo = Decimal("10000")
    rentepercentage = Decimal("3.65")
    datum = date(2025, 1, 1)

    dagrente = bereken_dagrente(
        saldo, rentepercentage, datum
    )

    assert dagrente == Decimal("1")


def test_dagrente_schrikkeljaar():
    """Controleert de dagrente in een schrikkeljaar."""
    saldo = Decimal("10000")
    rentepercentage = Decimal("3.66")
    datum = date(2024, 1, 1)

    dagrente = bereken_dagrente(
        saldo, rentepercentage, datum
    )

    assert dagrente == Decimal("1")
