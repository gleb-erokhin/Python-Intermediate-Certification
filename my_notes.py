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


def add_data(my_list):
    print("(Запись вводится через пробел)")
    # добавляем новую запись в конец
    my_list.append(input("Enter data \n").split())
    write_data(my_list)  # записываем данные
    menu(my_list)  # вызываем меню


def change_data(my_list):
    stop = True  # переменная для остановки цикла
    while stop:
        edit = int(input("chose record: \n"))  # выбираем запись в приложении Заметки
        for i in range(len(my_list)):  # цикл для прохода по записям и поиск порядкового номера
            if int(my_list[i][0]) == edit:  # находим нужный вложенный список по номеру заметки
                # удаляем вложенный список по индексу
                my_list.remove(my_list[i])
                # вставляем на место удаленного по индексу новый вводимый список
                my_list.insert(i, input("Enter new data \n").split())
                stop = False  # так как все сделано останавливаем while
                break  # выход из цикла
            else:
                continue  # нужен для продолжения поиска по введнному номеру заметки
    # так как вышли из цикла, записываем новые данные в файл
    write_data(my_list)






if __name__ == '__main__':
    main()