
# SVI Bank – Spaarrekening

## Over het project

Dit project is gemaakt voor Lesopdracht 6.1:
Codekwaliteit verbeteren en refactoren.

Het programma is geschreven in Python en berekent
rente over een spaarrekening.

## Functionaliteiten

- Dagelijkse rente berekenen
- Rekening houden met schrikkeljaren
- Rentepercentage bepalen op basis van het saldo
- Opgebouwde rente bijhouden
- Kwartaalrente uitkeren
- Dubbele kwartaaluitkeringen voorkomen
- Negatieve beginsaldi weigeren

## Projectstructuur

- `main.py` – Start het programma
- `rekening.py` – Beheert de spaarrekening
- `rente.py` – Bevat de renteberekeningen
- `tests/test_rente.py` – Bevat automatische tests

## Refactoring en codekwaliteit

Ik heb de code verbeterd door:

- Duidelijke functienamen te gebruiken
- De code op te splitsen in verschillende bestanden
- Een Rekening-klasse te gebruiken
- Docstrings en commentaar toe te voegen
- Ongebruikte imports te verwijderen
- Invoervalidatie toe te voegen
- De tests overzichtelijker te maken met pytest

## Testen

Ik gebruik pytest om het programma te testen.

Voer de tests uit met:

```bash
python -m pytest tests/test_rente.py -v
```

Bij de laatste controle zijn alle 22 tests geslaagd.

## Wat heb ik geleerd?

Ik heb geleerd hoe ik Python-code overzichtelijker
en beter onderhoudbaar kan maken.

Ook heb ik geleerd hoe belangrijk automatische tests
zijn om te controleren of wijzigingen goed werken.

Met Git en GitHub houd ik mijn wijzigingen bij.
