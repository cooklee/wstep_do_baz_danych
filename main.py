INTERFACE = """
1 - wypisz uzytkowników
2 - dodaj użytkownika
3 - wyjdz z programu

"""

while True:
    opcja = input(INTERFACE)
    if opcja == "1":
        print('tutaj wyświetle uzytkownikow')
    elif opcja == '2':
        print('tutaj dodam uzytkownikow')
    elif opcja == '3':
        print("do widzenia")
        break
    else:
        print("nie znam tej komendy")
