"""Wyświetlanie historii treningów i eksport danych do pliku CSV."""

import csv
import json

from trening import wczytaj_treningi


PLIK_CSV = "treningi.csv"


def eksportuj_csv(treningi):
    """Zapisuje listę treningów do pliku CSV."""
    if not treningi:
        print("Brak treningów do wyeksportowania.")
        return

    if not all(isinstance(trening, dict) for trening in treningi):
        print("Nie można wyeksportować danych: nieprawidłowy format treningów.")
        return

    kolumny = list(dict.fromkeys(
        klucz for trening in treningi for klucz in trening.keys()
    ))
    if not kolumny:
        print("Nie można wyeksportować danych: treningi nie mają pól.")
        return

    try:
        with open(PLIK_CSV, "w", newline="", encoding="utf-8-sig") as plik:
            zapis = csv.DictWriter(plik, fieldnames=kolumny, delimiter=";")
            zapis.writeheader()
            zapis.writerows(treningi)
    except (OSError, csv.Error, ValueError) as blad:
        print(f"Błąd eksportu CSV: {blad}")
        return

    print(f"Wyeksportowano {len(treningi)} treningów do pliku {PLIK_CSV}.")


def pokaz_historie():
    """Wyświetla historię i opcjonalnie eksportuje ją do CSV."""
    try:
        treningi = wczytaj_treningi()
    except (OSError, json.JSONDecodeError, UnicodeError) as blad:
        print(f"Nie udało się odczytać historii treningów: {blad}")
        return

    if not isinstance(treningi, list):
        print("Nieprawidłowy format pliku treningi.json (oczekiwano listy).")
        return

    if not treningi:
        print("Historia treningów jest pusta.")
        return

    print("\n=== HISTORIA TRENINGÓW ===")
    for numer, trening in enumerate(treningi, start=1):
        print(f"\nTrening {numer}:")
        if isinstance(trening, dict):
            for pole, wartosc in trening.items():
                print(f"  {pole}: {wartosc}")
        else:
            print(f"  {trening}")

    wybor = input("\nCzy wyeksportować historię do CSV? (t/n): ").strip().lower()
    if wybor == "t":
        eksportuj_csv(treningi)
    else:
        print("Powrót do menu głównego.")
