

import json

class Produkt:
    def __init__(self, nazwa, cena, kategoria, sztuki=10):
        self.nazwa = nazwa
        self.cena = float(cena)
        self.kategoria = kategoria
        self.sztuki = int(sztuki)

magazyn = [
    Produkt("mleko", 4.50, "spozywczy", 10),
    Produkt("sól", 2.50, "przyprawa", 0),
]

dane_do_zapisu = [{"nazwa": p.nazwa, "cena": p.cena, "kategoria": p.kategoria, "sztuki": p.sztuki} for p in magazyn]
with open("magazyn.json", "w", encoding="utf-8") as plik:
    json.dump(dane_do_zapisu, plik, ensure_ascii=False, indent=4)

print("zapisano do pliku")


while True:
    print("\n" + "=" * 40)
    print("           MENU SKLEPU")
    print("=" * 40)
    print("1 - Wszystkie produkty")
    print("2 - Dostępne produkty")
    print("3 - Wyszukaj produkt")
    print("4 - Produkty do podanej ceny")
    print("5 - Kup produkt")
    print("0 - Zakończ program")
    print("=" * 40)

    wybor = input("Wybierz opcję (0-5): ").strip()

    if wybor not in ["0", "1", "2", "3", "4", "5"]:
        print("Błąd: Wybrano złą opcję! Proszę wybrać wartość ze zbioru: 0, 1, 2, 3, 4, 5.")
        continue

    if wybor == "0":
        print("Dziękujemy za skorzystanie z programu. Do widzenia!")
        break

    elif wybor == "1":
        print("\n--- Wszystkie produkty ---")
        for p in magazyn:
            print(f"- {p.nazwa} | Kategoria: {p.kategoria} | Cena: {p.cena:.2f} zł | Sztuk: {p.sztuki}")

    elif wybor == "2":
        print("\n--- Dostępne produkty ---")
        znaleziono = False
        for p in magazyn:
            if p.sztuki > 0:
                znaleziono = True
                print(f"- {p.nazwa} | Kategoria: {p.kategoria} | Cena: {p.cena:.2f} zł | Sztuk: {p.sztuki}")
        if not znaleziono:
            print("Brak dostępnych produktów w magazynie.")

    elif wybor == "3":
        fraza = input("Podaj nazwę produktu lub fragment: ").strip().lower()
        print(f"\n--- Wyniki wyszukiwania dla '{fraza}' ---")
        znaleziono = False
        for p in magazyn:
            if fraza in p.nazwa.lower():
                znaleziono = True
                print(f"- {p.nazwa} | Kategoria: {p.kategoria} | Cena: {p.cena:.2f} zł | Sztuk: {p.sztuki}")
        if not znaleziono:
            print("nie znaleziono produktu")

    elif wybor == "4":
        cena_input = input("Podaj maksymalną cenę: ").strip().replace(",", ".")
        try:
            maks_cena = float(cena_input)
        except ValueError:
            print("Błąd: Podano nieprawidłową cenę.")
            continue

        print(f"\n--- Produkty o cenie do {maks_cena:.2f} zł ---")
        znaleziono = False
        for p in magazyn:
            if p.cena <= maks_cena:
                znaleziono = True
                print(f"- {p.nazwa} | Kategoria: {p.kategoria} | Cena: {p.cena:.2f} zł | Sztuk: {p.sztuki}")
        if not znaleziono:
            print("nie znaleziono produktu")

    elif wybor == "5":
        szukana_nazwa = input("podaj produkt: ").strip().lower()
        produkt_znaleziony = False

        for p in magazyn:
            if p.nazwa.lower() == szukana_nazwa:
                produkt_znaleziony = True
                if p.sztuki == 0:
                    print("produkt niedostepny")
                else:
                    p.sztuki -= 1
                    print(f"kupiono {p.nazwa}")
                    print(f"pozostalo sztuk: {p.sztuki}")
                break

        if not produkt_znaleziony:
            print("nie znaleziono produktu")
