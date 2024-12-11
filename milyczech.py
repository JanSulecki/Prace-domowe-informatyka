import random

# Funkcja powitalna
def powitanie():
    print("Witaj w grze 'Ekspedycja w Dżungli!'")
    print("Jako lider ekspedycji naukowej wyruszysz w podróż do nieznanej dżungli.")
    print("Twoje decyzje będą miały wpływ na bezpieczeństwo grupy i sukces misji.\n")

# Funkcja pytająca o decyzję
def pytanie(q, opcja_a, opcja_b, odpowiedz_poprawna):
    print(q)
    print(f"A) {opcja_a}")
    print(f"B) {opcja_b}")
    
    wybor = input("Wybierz A lub B: ").upper()
    
    while wybor not in ['A', 'B']:
        print("Niepoprawny wybór. Wybierz A lub B.")
        wybor = input("Wybierz A lub B: ").upper()
    
    if wybor == odpowiedz_poprawna:
        print("Dobra decyzja! Kontynuujemy ekspedycję.\n")
        return True
    else:
        print("Błąd! Twoja decyzja może wpłynąć na bezpieczeństwo ekspedycji.\n")
        return False

# Funkcja do obliczania zasobów
def oblicz_zasoby(zasoby, ryzyko):
    szansa = random.randint(1, 100)
    if szansa <= ryzyko:
        zasoby += random.randint(10, 50)
    else:
        zasoby -= random.randint(5, 20)
    return zasoby

# Funkcja do wprowadzenia gracza do gry
def wprowadzenie_do_gry():
    print("Twoja ekspedycja wyrusza na badanie nieznanej dżungli.")
    print("Musisz podejmować decyzje dotyczące bezpieczeństwa, zarządzania zasobami i interakcji z dziką fauną.")
    input("Naciśnij Enter, aby rozpocząć podróż...")

# Funkcja główna
def gra():
    powitanie()
    wprowadzenie_do_gry()
    
    zasoby = 100  # Początkowe zasoby (jedzenie, woda, sprzęt)
    ryzyko = 30  # Początkowe ryzyko (prawdopodobieństwo zagrożeń)

    # Gra toczy się przez 45 etapów
    for etap in range(1, 41):
        print(f"Etap {etap}:\n")
        
        if etap == 1:
            if pytanie("Ekspedycja trafia na rzekę. Czy chcesz spróbować ją przepłynąć?", "Tak", "Nie", "A"):
                zasoby -= 20
            else:
                zasoby -= 10
        
        elif etap == 2:
            if pytanie("Zespół spotyka dzikie zwierzęta. Czy chcesz spróbować je oswoić?", "Tak", "Nie", "B"):
                zasoby -= 30
            else:
                zasoby += 10

        elif etap == 3:
            if pytanie("Czy chcesz zbudować obozowisko na noc?", "Tak", "Nie", "A"):
                zasoby += 20
            else:
                zasoby -= 10

        elif etap == 4:
            if pytanie("Napotkano wulkan. Czy chcesz go zbadać?", "Tak", "Nie", "B"):
                zasoby -= 50
                ryzyko += 20
            else:
                zasoby += 10

        elif etap == 5:
            if pytanie("Czy chcesz wziąć próbki roślin do analizy?", "Tak", "Nie", "A"):
                zasoby += 30
            else:
                zasoby += 5

        elif etap == 6:
            if pytanie("Znalazłeś tropy zwierząt. Czy chcesz je śledzić?", "Tak", "Nie", "B"):
                zasoby -= 40
                ryzyko += 10
            else:
                zasoby += 15

        elif etap == 7:
            if pytanie("Podczas wędrówki załamuje się pogoda. Czy chcesz przeczekać burzę?", "Tak", "Nie", "A"):
                zasoby -= 10
            else:
                zasoby += 5

        elif etap == 8:
            if pytanie("Zespół znajduje ukrytą świątynię. Czy chcesz ją zbadać?", "Tak", "Nie", "A"):
                zasoby += 100
            else:
                zasoby += 20

        elif etap == 9:
            if pytanie("Czy chcesz spróbować przejść przez nieznaną dolinę?", "Tak", "Nie", "B"):
                zasoby -= 50
                ryzyko += 15
            else:
                zasoby += 10

        elif etap == 10:
            if pytanie("W końcu natrafiliście na starożytną ruiny. Czy chcesz zabrać próbki artefaktów?", "Tak", "Nie", "A"):
                zasoby += 200
            else:
                zasoby += 50

        elif etap == 11:
            if pytanie("Ekspedycja napotyka groźną rzekę. Czy zdecydujesz się ją przepłynąć?", "Tak", "Nie", "A"):
                zasoby -= 20
            else:
                zasoby -= 10

        elif etap == 12:
            if pytanie("Czy chcesz wysłać zwiadowców na przednią linię, aby zbadać teren?", "Tak", "Nie", "A"):
                zasoby -= 15
            else:
                zasoby += 5

        elif etap == 13:
            if pytanie("Ekspedycja spotyka plemię lokalnych mieszkańców. Czy chcesz nawiązać kontakt?", "Tak", "Nie", "A"):
                zasoby += 50
            else:
                zasoby -= 10

        elif etap == 14:
            if pytanie("W zaroślach napotykasz niebezpieczne węże. Czy chcesz je unikać?", "Tak", "Nie", "A"):
                zasoby -= 10
            else:
                zasoby -= 50

        elif etap == 15:
            if pytanie("Czy chcesz spróbować przekroczyć góry?", "Tak", "Nie", "B"):
                zasoby -= 60
                ryzyko += 25
            else:
                zasoby += 15

        elif etap == 16:
            if pytanie("Zespół napotyka ogromną wodospad. Czy spróbujesz go zbadać?", "Tak", "Nie", "B"):
                zasoby -= 40
                ryzyko += 20
            else:
                zasoby += 10

        elif etap == 17:
            if pytanie("Znalazłeś nieznane rośliny. Czy chcesz je zabrać na badania?", "Tak", "Nie", "A"):
                zasoby += 25
            else:
                zasoby += 5

        elif etap == 18:
            if pytanie("Zespół spotyka dzikiego jaguara. Czy chcesz spróbować go przechytrzyć?", "Tak", "Nie", "B"):
                zasoby -= 40
            else:
                zasoby += 15

        elif etap == 19:
            if pytanie("Czy chcesz spróbować schronić się w jaskini, która wygląda na bezpieczną?", "Tak", "Nie", "A"):
                zasoby += 20
            else:
                zasoby -= 15

        elif etap == 20:
            if pytanie("Czy chcesz poszukać wody w pobliżu?", "Tak", "Nie", "A"):
                zasoby += 10
            else:
                zasoby -= 20

        elif etap == 21:
            if pytanie("Ekspedycja trafia na duże złoża minerałów. Czy chcesz je zabrać?", "Tak", "Nie", "A"):
                zasoby += 50
            else:
                zasoby += 15

        elif etap == 22:
            if pytanie("Czy chcesz zabrać mapę starożytnej cywilizacji?", "Tak", "Nie", "A"):
                zasoby += 50
            else:
                zasoby += 10

        elif etap == 23:
            if pytanie("Czy chcesz spróbować wyjść z dżungli przez nieznany wąwóz?", "Tak", "Nie", "B"):
                zasoby -= 30
                ryzyko += 30
            else:
                zasoby += 10

        elif etap == 24:
            if pytanie("Znalazłeś jaskinię pełną rzadkich skarbów. Czy chcesz je zabrać?", "Tak", "Nie", "A"):
                zasoby += 100
            else:
                zasoby += 20

        elif etap == 25:
            if pytanie("Zespół napotyka na gorące źródła. Czy zdecydujesz się wykopać próbki?", "Tak", "Nie", "A"):
                zasoby += 30
            else:
                zasoby -= 5

        elif etap == 26:
            if pytanie("Zespół napotyka zagrożenie ze strony bandytów. Czy spróbujesz się bronić?", "Tak", "Nie", "A"):
                zasoby -= 50
            else:
                zasoby += 5

        elif etap == 27:
            if pytanie("Napotkano starożytną platformę. Czy zdecydujesz się na niej rozbić oboz?", "Tak", "Nie", "A"):
                zasoby += 20
            else:
                zasoby -= 5

        elif etap == 28:
            if pytanie("Czy chcesz spróbować złapać dzikie zwierzę?", "Tak", "Nie", "B"):
                zasoby -= 30
            else:
                zasoby += 10

        elif etap == 29:
            if pytanie("Natrafiłeś na trudny teren do przejścia. Czy zdecydujesz się na obejście?", "Tak", "Nie", "A"):
                zasoby += 10
            else:
                zasoby -= 20

        elif etap == 30:
            if pytanie("Spotkaliście niewielki wodospad. Czy zdecydujesz się go zbadać?", "Tak", "Nie", "A"):
                zasoby += 15
            else:
                zasoby -= 5
        
        elif etap == 31:
            if pytanie("Zespół znajduje starożytną mapę. Czy chcesz ją zabrać?", "Tak", "Nie", "A"):
                zasoby += 50
            else:
                zasoby += 10

        elif etap == 32:
            if pytanie("Ekspedycja spotyka dzikie zwierzęta. Czy chcesz je zaobserwować?", "Tak", "Nie", "A"):
                zasoby -= 10
            else:
                zasoby += 5

        elif etap == 33:
            if pytanie("Zespół natrafia na ogromną rzekę. Czy spróbujesz ją przepłynąć?", "Tak", "Nie", "B"):
                zasoby -= 40
                ryzyko += 30
            else:
                zasoby += 15

        elif etap == 34:
            if pytanie("Spotkaliście grupę lokalnych przewoźników. Czy chcesz wynająć transport?", "Tak", "Nie", "A"):
                zasoby -= 60
            else:
                zasoby += 20

        elif etap == 35:
            if pytanie("Zespół napotyka nieznaną roślinność. Czy chcesz je zbadać?", "Tak", "Nie", "A"):
                zasoby += 20
            else:
                zasoby += 5

        elif etap == 36:
            if pytanie("Spotkaliście niebezpiecznych piratów. Czy spróbujesz uciekać?", "Tak", "Nie", "A"):
                zasoby -= 30
            else:
                zasoby -= 60

        elif etap == 37:
            if pytanie("Zespół znajduje nieznane zwierzęta. Czy zdecydujesz się je złapać?", "Tak", "Nie", "B"):
                zasoby -= 50
            else:
                zasoby += 20

        elif etap == 38:
            if pytanie("W dżungli zaczyna się zbliżać pożar. Czy chcesz spróbować go ugasić?", "Tak", "Nie", "A"):
                zasoby -= 40
            else:
                zasoby += 10

        elif etap == 39:
            if pytanie("Zespół napotyka grupę zaginionych podróżników. Czy chcesz im pomóc?", "Tak", "Nie", "A"):
                zasoby += 30
            else:
                zasoby -= 10

        elif etap == 40:
            if pytanie("Znalazłeś starożytny artefakt. Czy zdecydujesz się go zabrać?", "Tak", "Nie", "A"):
                zasoby += 150
            else:
                zasoby += 20




        # Dodatkowe etapy w podobny sposób do etapu 30-45

        # Gra kończy się, jeśli zasoby spadną do zera.
        if zasoby <= 0:
            print("\nNiestety, Twoja ekspedycja zakończyła się niepowodzeniem. Brak zasobów!")
            break
        
        print(f"Zasoby po etapie {etap}: {zasoby}")
    
    else:
        print("\nGratulacje! Udało Ci się zakończyć ekspedycję z wystarczającymi zasobami.")

# Uruchomienie gry
gra()
