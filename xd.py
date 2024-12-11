import random

# Funkcja powitalna
def powitanie():
    print("Witaj w grze 'Zarabiaj milion'!")
    print("Twoim celem jest zarobić milion.")
    print("Wybieraj odpowiedzi A lub B, aby podejmować decyzje, które poprowadzą cię do celu.")
    print("Powodzenia!\n")

# Funkcja pytająca o decyzję
def pytanie(q, opcja_a, opcja_b, odpowiedz_poprawna):
    print(q)
    print("A) " + opcja_a)
    print("B) " + opcja_b)
    
    wybor = input("Wybierz A lub B: ").upper()
    
    while wybor not in ['A', 'B']:
        print("Niepoprawny wybór. Wybierz A lub B.")
        wybor = input("Wybierz A lub B: ").upper()
    
    if wybor == odpowiedz_poprawna:
        print("Brawo! Podejmujesz dobrą decyzję.\n")
        return True
    else:
        print("Błąd! To nie była dobra decyzja.\n")
        return False

# Funkcja do obliczania zarobków
def oblicz_zarobki(zarobek, ryzyko):
    szansa = random.randint(1, 100)
    if szansa <= ryzyko:
        zarobek += random.randint(50000, 200000)
    else:
        zarobek -= random.randint(10000, 50000)
    return zarobek

# Funkcja do losowania bonusu
def bonus():
    print("Wykorzystujesz swoją szansę na dodatkowy bonus!")
    if random.random() > 0.5:
        print("Bonus! Dodatkowe pieniądze za mądrość!")
        return random.randint(50000, 150000)
    else:
        print("Niestety, bonusu nie ma. Straciłeś trochę pieniędzy.")
        return random.randint(-50000, -20000)

# Funkcja wprowadzająca gracza w świat gry
def wprowadzenie_do_gry():
    print("Witaj w wirtualnym świecie biznesu! Twoim celem jest zarobić milion.")
    print("Zaczynasz od małej firmy. Decyzje, które podejmujesz, będą miały ogromny wpływ na twoje finanse.")
    print("Pamiętaj, nie każda decyzja jest łatwa, ale od Ciebie zależy, jak rozwiniesz swój biznes.")
    print("W każdej chwili możesz zaryzykować więcej lub działać bezpiecznie.")
    print("Czy jesteś gotowy? Zaczynajmy!")
    input("\nNaciśnij Enter, aby rozpocząć...")

# Funkcja główna
def gra():
    powitanie()
    wprowadzenie_do_gry()
    
    zarobek = 0
    ryzyko = 50  # Początkowe ryzyko

    # Etap 1
    print("Etap 1: Zaczynasz swoją podróż jako początkujący przedsiębiorca.")
    if pytanie("Czy chcesz zainwestować w nieruchomości?", "Tak", "Nie", "A"):
        zarobek += 100000
    else:
        zarobek += 20000
    print(f"Zarobki po etapie 1: {zarobek}\n")

    # Etap 2
    print("Etap 2: Masz do wyboru inwestycję w reklamę lub rozwój produktów.")
    if pytanie("Czy chcesz zainwestować w reklamę internetową?", "Tak", "Nie", "A"):
        zarobek = oblicz_zarobki(zarobek, ryzyko)
    else:
        zarobek += 10000
    print(f"Zarobki po etapie 2: {zarobek}\n")

    # Etap 3
    print("Etap 3: Pojawia się możliwość przejęcia innej firmy.")
    if pytanie("Czy chcesz przejąć konkurencyjną firmę?", "Tak", "Nie", "A"):
        zarobek += 300000
        ryzyko += 20
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 3: {zarobek}\n")

    # Etap 4 - Ryzykowna inwestycja
    print("Etap 4: Ryzykowna inwestycja.")
    if pytanie("Czy chcesz zainwestować w ryzykowny startup?", "Tak", "Nie", "A"):
        zarobek = oblicz_zarobki(zarobek, ryzyko)
    else:
        zarobek += 15000
    print(f"Zarobki po etapie 4: {zarobek}\n")

    # Etap 5 - Bonus
    print("Etap 5: Czas na decyzję o bonusie.")
    zarobek += bonus()
    print(f"Zarobki po etapie 5: {zarobek}\n")

    # Etap 6 - Duża inwestycja
    print("Etap 6: Kolejna duża inwestycja w nowe technologie.")
    if pytanie("Czy chcesz zainwestować w nowe technologie?", "Tak", "Nie", "A"):
        zarobek += 500000
    else:
        zarobek += 10000
    print(f"Zarobki po etapie 6: {zarobek}\n")

    # Etap 7 - Konkurs
    print("Etap 7: Konkurs na najlepszy produkt.")
    if pytanie("Czy chcesz zainwestować w konkurs na nowy produkt?", "Tak", "Nie", "A"):
        zarobek += 200000
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 7: {zarobek}\n")

    # Etap 8 - Kłopoty finansowe
    print("Etap 8: Twoja firma ma problemy finansowe.")
    if pytanie("Czy chcesz pożyczyć pieniądze na pokrycie długu?", "Tak", "Nie", "A"):
        zarobek += 100000
    else:
        zarobek -= 50000
    print(f"Zarobki po etapie 8: {zarobek}\n")
    
    # Etap 10 - Nowa strategia marketingowa
    print("Etap 10: Tworzysz nową strategię marketingową.")
    if pytanie("Czy chcesz zainwestować w reklamy na dużą skalę?", "Tak", "Nie", "A"):
        zarobek += 150000
    else:
        zarobek += 30000
    print(f"Zarobki po etapie 10: {zarobek}\n")

    # Etap 11 - Inwestycja w sztuczną inteligencję
    print("Etap 11: Możliwość inwestycji w sztuczną inteligencję.")
    if pytanie("Czy chcesz zainwestować w rozwój AI?", "Tak", "Nie", "A"):
        zarobek += 250000
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 11: {zarobek}\n")

    # Etap 12 - Zatrudnianie ekspertów
    print("Etap 12: Zatrudniasz ekspertów do swojego zespołu.")
    if pytanie("Czy chcesz zatrudnić najlepszych specjalistów?", "Tak", "Nie", "A"):
        zarobek += 200000
    else:
        zarobek += 30000
    print(f"Zarobki po etapie 12: {zarobek}\n")

    # Etap 13 - Nowa lokalizacja
    print("Etap 13: Rozważasz otwarcie nowej lokalizacji.")
    if pytanie("Czy chcesz otworzyć sklep w innym mieście?", "Tak", "Nie", "A"):
        zarobek += 150000
    else:
        zarobek += 20000
    print(f"Zarobki po etapie 13: {zarobek}\n")

    # Etap 14 - Zmiana branży
    print("Etap 14: Decyzja o zmianie branży.")
    if pytanie("Czy chcesz zmienić branżę na bardziej dochodową?", "Tak", "Nie", "A"):
        zarobek += 300000
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 14: {zarobek}\n")

    # Etap 15 - Kryzys gospodarczy
    print("Etap 15: Zaczynasz odczuwać kryzys gospodarczy.")
    if pytanie("Czy chcesz zredukować koszty poprzez zwolnienia?", "Tak", "Nie", "A"):
        zarobek -= 50000
    else:
        zarobek -= 100000
    print(f"Zarobki po etapie 15: {zarobek}\n")

    # Etap 16 - Nowa technologia
    print("Etap 16: Pojawia się nowa, rewolucyjna technologia.")
    if pytanie("Czy chcesz zainwestować w nową technologię?", "Tak", "Nie", "A"):
        zarobek += 400000
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 16: {zarobek}\n")

    # Etap 17 - Problem z dostawcami
    print("Etap 17: Twój główny dostawca ma problemy.")
    if pytanie("Czy chcesz zmienić dostawcę, ryzykując wyższymi kosztami?", "Tak", "Nie", "A"):
        zarobek -= 50000
    else:
        zarobek -= 20000
    print(f"Zarobki po etapie 17: {zarobek}\n")

    # Etap 18 - Działania ekologiczne
    print("Etap 18: Przechodzisz na ekologiczne rozwiązania.")
    if pytanie("Czy chcesz zainwestować w zieloną energię?", "Tak", "Nie", "A"):
        zarobek += 100000
    else:
        zarobek += 20000
    print(f"Zarobki po etapie 18: {zarobek}\n")

    # Etap 19 - Współpraca z influencerem
    print("Etap 19: Współpraca z influencerem.")
    if pytanie("Czy chcesz zainwestować w reklamę u znanego influencera?", "Tak", "Nie", "A"):
        zarobek += 150000
    else:
        zarobek += 30000
    print(f"Zarobki po etapie 19: {zarobek}\n")

    # Etap 20 - Przyciąganie inwestorów
    print("Etap 20: Szukasz inwestorów do dalszego rozwoju.")
    if pytanie("Czy chcesz pozyskać inwestora zewnętrznego?", "Tak", "Nie", "A"):
        zarobek += 500000
    else:
        zarobek += 100000
    print(f"Zarobki po etapie 20: {zarobek}\n")

    # Etap 21 - Globalizacja
    print("Etap 21: Twoja firma zaczyna myśleć o globalizacji.")
    if pytanie("Czy chcesz otworzyć biuro w innych krajach?", "Tak", "Nie", "A"):
        zarobek += 400000
    else:
        zarobek += 100000
    print(f"Zarobki po etapie 21: {zarobek}\n")

    # Etap 22 - Kryzys zdrowotny
    print("Etap 22: Nagle pojawia się kryzys zdrowotny, który wpływa na Twoją firmę.")
    if pytanie("Czy chcesz wprowadzić zmiany w organizacji, by poradzić sobie z kryzysem?", "Tak", "Nie", "A"):
        zarobek -= 100000
    else:
        zarobek -= 50000
    print(f"Zarobki po etapie 22: {zarobek}\n")

    # Etap 23 - Nowy konkurent
    print("Etap 23: Pojawia się nowy konkurent, który zdobywa rynek.")
    if pytanie("Czy chcesz podjąć agresywną kampanię reklamową, by pokonać konkurencję?", "Tak", "Nie", "A"):
        zarobek += 200000
    else:
        zarobek += 50000
    print(f"Zarobki po etapie 23: {zarobek}\n")

    # Etap 24 - Partnerstwo z gigantem
    print("Etap 24: Na rynku pojawia się możliwość partnerstwa z dużą firmą.")
    if pytanie("Czy chcesz połączyć siły z gigantem branży?", "Tak", "Nie", "A"):
        zarobek += 600000
    else:
        zarobek += 200000
    print(f"Zarobki po etapie 24: {zarobek}\n")

    # Etap 25 - Złamanie prawa
    print("Etap 25: Jeden z Twoich pracowników łamie prawo.")
    if pytanie("Czy chcesz przejąć odpowiedzialność za jego czyny?", "Tak", "Nie", "B"):
        zarobek -= 150000
    else:
        zarobek -= 50000
    print(f"Zarobki po etapie 25: {zarobek}\n")

    # Etap 26 - Nagła sprzedaż
    print("Etap 26: Przychodzi oferta sprzedaży Twojej firmy.")
    if pytanie("Czy chcesz sprzedać firmę za dużą kwotę?", "Tak", "Nie", "A"):
        zarobek += 1000000
        print("Gratulacje! Zarobiłeś milion!")
    else:
        zarobek += 200000
    print(f"Zarobki po etapie 26: {zarobek}\n")

    # Etap 27 - Kradzież danych
    print("Etap 27: Firma padła ofiarą cyberataków.")
    if pytanie("Czy chcesz zainwestować w bezpieczeństwo cyfrowe?", "Tak", "Nie", "A"):
        zarobek -= 100000
    else:
        zarobek -= 200000
    print(f"Zarobki po etapie 27: {zarobek}\n")

    # Etap 28 - Nowe biuro
    print("Etap 28: Otwierasz nowe biuro w prestiżowej dzielnicy.")
    if pytanie("Czy chcesz wynająć biuro w luksusowej lokalizacji?", "Tak", "Nie", "A"):
        zarobek -= 200000
    else:
        zarobek -= 50000
    print(f"Zarobki po etapie 28: {zarobek}\n")

    # Etap 29 - Problemy z rynkiem
    print("Etap 29: Rynek zaczyna się kurczyć.")
    if pytanie("Czy chcesz zainwestować w nowe rynki?", "Tak", "Nie", "A"):
        zarobek += 250000
    else:
        zarobek -= 50000
    print(f"Zarobki po etapie 29:{zarobek}\n")


    # Etap 9 - Przejęcie firmy
    print("Etap 9: Wykorzystaj okazję przejęcia dużej firmy.")
    if pytanie("Czy chcesz przejąć dużą firmę?", "Tak", "Nie", "A"):
        zarobek += 1000000
        print("Gratulacje! Zarobiłeś milion!")
    else:
        zarobek += 500000
        print("Zarobiłeś dużo pieniędzy, ale nie osiągnąłeś miliona.")
    
    print(f"Zarobki na koniec gry: {zarobek}\n")

    if zarobek >= 1000000:
        print("Gratulacje! Zarobiłeś milion!")
    else:
        print("Niestety, nie udało ci się zarobić miliona. Ale nie martw się, masz szansę na więcej w przyszłości.")

    print("Dziękuję za grę!")

# Rozpoczęcie gry
gra()