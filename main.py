def wyswietl_menu():
    print("\n=== FIT TRACK ===")
    print("1. Dodaj trening")
    print("2. Kalkulator BMI i kalorii")
    print("3. Pokaż statystyki")
    print("0. Wyjście")


def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "0":
            print("Do zobaczenia na treningu!")
            break
        else:
            print("Funkcjonalność w trakcie budowy...")


if __name__ == "__main__":
    main()
