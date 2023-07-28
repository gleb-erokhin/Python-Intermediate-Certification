*Промежуточная контрольная работа по языку Python*

1. Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. 
2. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). 
3. Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.

***Реализация приложения***

1. Приложение консольное, работа происходит через командную строку
2. Для начала работы необходим пустой файл csv, с именем: **notes.csv**
3. Файл **my_notes.py** - содержит основной код программы.
4. После запуска приложения, мы видим меню из 4х пунктов, каждый пункт пронумерован для осуществления выбора нужного.
5. Меню приложения: 
   1. ***1*** - **показать все записи**, 
   2. ***2*** - **добавить запись**, 
   3. ***3*** - **изменить запись**, 
   4. ***4*** - **выход**.
6. Добавление записи формируется по шаблону, *(пользователь сам придумывает ИДЕНТИФИКАТОР, фильтрации ввода нет)*: 
   1. идентификатор записи ___***пробел***___ текст записи ___***пробел***___ дата записи.
   2. ___***ИДЕНТИФИКАТОР***___ имеет важное значение по нему происходит добавление и изменение записи, он должен быть валидный и легко узнаваем.