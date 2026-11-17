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
    aktywnosc = input("Rodzaj aktywności (np. bieganie): ")
    try:
        minuty = int(input("Czas trwania (minuty): "))
        kalorie = int(input("Spalone kalorie (kcal): "))
    except ValueError:
        print("Błąd: podaj liczbę całkowitą.")
        return
    treningi = wczytaj_treningi()
    treningi.append({"data": str(date.today()), "aktywnosc": aktywnosc,
                     "minuty": minuty, "kalorie": kalorie})
    with open(PLIK, "w", encoding="utf-8") as f:
        json.dump(treningi, f, ensure_ascii=False, indent=2)
    print("Trening zapisany!")
