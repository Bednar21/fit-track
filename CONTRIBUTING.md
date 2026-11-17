Zasady współpracy (Contributing Guidelines)

Aby zachować porządek w repozytorium, wszyscy członkowie zespołu zobowiązani są do przestrzegania poniższych zasad:

## 1. Przepływ pracy (Workflow)
1. Wykonaj **Fork** głównego repozytorium na swoje konto GitHub.
2. Sklonuj swój fork lokalnie (`git clone ...`).
3. Dla każdego zadania utwórz nową gałąź roboczą z gałęzi `main`.
4. Po zakończeniu prac wypchnij gałąź na swój fork i utwórz **Pull Request (PR)** do głównego repozytorium.

## 2. Nazewnictwo gałęzi (Branches)
Nazwy gałęzi powinny odzwierciedlać rodzaj i nazwę zadania:
- `feature/nazwa-funkcjonalnosci` (np. `feature/bmi-calculator`)
- `fix/opis-bledu` (np. `fix/input-validation`)
- `docs/opis-zmian` (np. `docs/update-readme`)

## 3. Zasady commitów
- Twórz małe, logiczne commity opisujące konkretną zmianę.
- Wiadomości commitów pisz w trybie rozkazującym, np.:
  - `Add BMI calculation function`
  - `Fix crash on empty user input`

## 4. Pull Requesty (PR)
Każdy Pull Request przed zmergowaniem musi zawierać:
- Czytelny tytuł opisujący zmianę.
- Krótki opis wykonanych prac.
- Link do powiązanej karty w Trello.
- Informację o ewentualnych problemach lub ograniczeniach.

## 5. Podział plików
- Każdy edytuje tylko swój moduł (`trening.py`, `bmi.py`, `statystyki.py`, `historia.py`) i swoją sekcję w README.
- Przed utworzeniem nowej gałęzi pobierz zmiany: `git pull upstream main`.
- Pull Requesty przegląda i scala Project Manager.
