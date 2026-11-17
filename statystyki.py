from trening import wczytaj_treningi


def pokaz_statystyki():
    treningi = wczytaj_treningi()
    if not treningi:
        print("Brak zapisanych treningów.")
        return
    minuty = sum(t["minuty"] for t in treningi)
    kalorie = sum(t["kalorie"] for t in treningi)
    print(f"Liczba treningów: {len(treningi)}")
    print(f"Łączny czas: {minuty} min")
    print(f"Łącznie spalone: {kalorie} kcal")
    print(f"Średnio na trening: {kalorie / len(treningi):.0f} kcal")