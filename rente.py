
from datetime import date


def is_schrikkeljaar(jaar):
    """Controleert of een jaar een schrikkeljaar is."""
    return jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0)


def aantal_dagen_in_jaar(datum):
    """Geeft het aantal dagen van het opgegeven jaar terug."""
    if is_schrikkeljaar(datum.year):
        return 366

    return 365
