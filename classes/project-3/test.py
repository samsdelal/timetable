from solution import LoadClass, AddClass, NsuClasses

q = NsuClasses('19704', '2') #Выводим расписание
r = LoadClass #Загружаем словарь с раписание из файла class.txt
q = AddClass.add_class(r) #Добавляем в расписание новые группы и подгруппы

print(q)