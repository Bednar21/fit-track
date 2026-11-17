# FitTrack 🏋️‍♂️

Aplikacja konsolowa napisana w języku Python służąca do monitorowania aktywności fizycznej, liczenia spalonych kalorii oraz śledzenia celów treningowych.

## 📋 Funkcjonalności
- Rejestrowanie treningów (rodzaj aktywności, czas trwania, spalone kalorie)
- Kalkulator BMI oraz zapotrzebowania kalorycznego (BMR)
- Zapis i odczyt historii treningów (JSON/CSV)
- Generowanie podsumowań i statystyk postępów

## 🛠️ Wykorzystane technologie
- **Język:** Python 3.10+
- **Biblioteki standardowe:** `json`, `csv`, `datetime`
- **Narzędzia:** Git, GitHub, Trello

## 🚀 Instrukcja uruchomienia
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Bednar21/fit-track.git
   cd fit-track
   ```
2. Uruchom aplikację (Python 3.10+):
   ```bash
   python main.py
   ```

## 👥 Skład zespołu
- Adam – Project Manager (repozytorium, Trello, przegląd i scalanie PR)
- Oliwier – dodawanie treningów (`trening.py`)
- Mateusz – kalkulator BMI i BMR (`bmi.py`)
- Filip – statystyki (`statystyki.py`)
- Kamil – historia i eksport CSV (`historia.py`)

## 🧩 Moduły

### trening.py – Oliwier
Opcja 1 w menu. Pyta o rodzaj aktywności, czas trwania i spalone kalorie,
a następnie zapisuje trening z dzisiejszą datą do pliku `treningi.json`.

### bmi.py – Mateusz
_do uzupełnienia_

### statystyki.py – Filip
_do uzupełnienia_

### historia.py – Kamil
_do uzupełnienia_
