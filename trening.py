# trening.py
import json
import os
from datetime import date

PLIK = "treningi.json"


def wczytaj_treningi():
    if not os.path.exists(PLIK):
        return []
    with open(PLIK, encoding="utf-8") as f:
        return json.load(f)


def dodaj_trening():
    print("Funkcjonalność w trakcie budowy...")
