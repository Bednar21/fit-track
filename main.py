import bmi
import historia
import statystyki
import trening


def wyswietl_menu():
    print("\n=== FIT TRACK ===")
    print("1. Dodaj trening")
    print("2. Kalkulator BMI i kalorii")
    print("3. Pokaż statystyki")
    print("4. Historia treningów")
    print("0. Wyjście")


def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "0":
            print("Do zobaczenia na treningu!")
            break
        elif wybor == "1":
            trening.dodaj_trening()
        elif wybor == "2":
            bmi.kalkulator()
        elif wybor == "3":
            statystyki.pokaz_statystyki()
        elif wybor == "4":
            historia.pokaz_historie()
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()
