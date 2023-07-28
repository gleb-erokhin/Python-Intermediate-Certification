import csv
# for csv file in VSC use plugin rainbowCSV
# структура файла csv принята такой:
# 2(порядковый номер записи),Текст записи,Дата записи

def menu(list):
    routine = True
    while routine:
        print("")
        print("The main menu")
        print("1 - Print all notes")
        print("2 - Add note")
        print("3 - Change note")
        print("4 - Exit")
        command = int(input("Choose number \n"))
        print("")
        if command == 1:  # повторная печать после изменений
            data = read_data()
            print_data(data)
        elif command == 2:
            add_data(list)  # для добавления записи
        elif command == 3:
            change_data(list)  # для изменения записи
        elif command == 4:  # выход из программы
            routine = False
            break

if __name__ == '__main__':
    main()