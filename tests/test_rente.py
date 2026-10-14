from decimal import Decimal
from rente import bereken_dagrente
from datetime import date
from rente import is_schrikkeljaar, aantal_dagen_in_jaar
from rente import bepaal_renteaanpassing, bepaal_rentepercentage
from rekening import Rekening

def test_eerste_saldoklasse():
    saldo = Decimal("5000")
    assert bepaal_renteaanpassing(saldo) == Decimal("-0.25")


def test_tweede_saldoklasse():
    saldo = Decimal("15000")
    assert bepaal_renteaanpassing(saldo) == Decimal("0")


def test_derde_saldoklasse():
    saldo = Decimal("30000")
    assert bepaal_renteaanpassing(saldo) == Decimal("-0.15")


def test_vierde_saldoklasse():
    saldo = Decimal("75000")
    assert bepaal_renteaanpassing(saldo) == Decimal("-0.25")


def test_vijfde_saldoklasse():
    saldo = Decimal("150000")
    assert bepaal_renteaanpassing(saldo) == Decimal("-0.50")


def test_boven_miljoen():
    saldo = Decimal("1500000")
    assert bepaal_renteaanpassing(saldo) is None


def test_rentepercentage():
    saldo = Decimal("15000")
    basisrente = Decimal("1.8")

    assert bepaal_rentepercentage(
        saldo, basisrente
    ) == Decimal("1.8")


def test_negatief_saldo():
    import pytest

    with pytest.raises(ValueError):
        bepaal_renteaanpassing(Decimal("-100"))



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

    
def test_rente_wordt_opgebouwd():
    """Controleert of rente apart wordt opgeslagen."""

    rekening = Rekening("15000")
    datum = date(2025, 1, 1)
    basisrente = Decimal("1.8")

    rekening.bereken_rente(datum, basisrente)

    assert rekening.toon_opgebouwde_rente() > 0


def test_saldo_blijft_gelijk():
    """Controleert of de rente niet direct wordt bijgeschreven."""

    rekening = Rekening("15000")
    datum = date(2025, 1, 1)
    basisrente = Decimal("1.8")

    rekening.bereken_rente(datum, basisrente)

    assert rekening.toon_saldo() == Decimal("15000")
