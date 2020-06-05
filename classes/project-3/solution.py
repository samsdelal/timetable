# -*- coding: utf-8 -*-

import json


class LoadClass:
    def __init__(self):

        f = open('class.txt', 'r')
        try:
            self.nus_classes = json.loads(f.read())
            self.week = {1: 'Пн', 2: 'Вт', 3: 'Ср', 4: 'Чт', 5: 'Пт', 6: 'Сб'}
            self.keys = list(self.nus_classes.keys())
        except ValueError:
            self.nus_classes = {}

    def __repr__(self):
        return str(self.nus_classes)


class AddClass(LoadClass):
    def add_class(self):
        LoadClass.__init__(self)
        group = input('Введите номер группы ')
        if group not in self.keys:
            self.nus_classes[group] = {}
        pod_group = input('Введите номер подгруппы ')
        self.nus_classes[group][pod_group] = {}
        for i in range(1, 7):
            self.week = {1: 'Пн', 2: 'Вт', 3: 'Ср', 4: 'Чт', 5: 'Пт', 6: 'Сб'}
            for b in range(1, 7):
                exist = input(f'Есть ли у вас {b} пара в {self.week[i]}\n1 - Да, 2 - Нет')
                if exist == '2':
                    continue
                if exist == '1':
                    z = {}
                    subject = input('Введите название предмета')
                    prepod = input('Введите имя преподавателя ')
                    room = input('Введите номер комнаты ')
                    z['Предмет'] = subject
                    z['Преподаватель'] = prepod
                    z['Кабинет'] = room
                    self.nus_classes[group][pod_group][self.week[i]] = z
        with open('class.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(self.nus_classes))
    def __str__(self):
        return str(self.nus_classes)

class NsuClasses(LoadClass):


    def __init__(self, group, pod_group):
        LoadClass.__init__(self)
        self.group = group
        self.pod_group = pod_group
    def __str__(self):
        q = f'Группа {self.group}.{self.pod_group}\n\n'
        for i in range(1, 7):
            q += self.week[i]+'\n'
            q += '-----------------------------\n'
            for b in range(1, 7):
                try:
                    q += f'{b} пара | Предмет - {str(self.nus_classes[self.group][self.pod_group][self.week[i]][str(b)]["Предмет"])} | Преподаватель - {str(self.nus_classes[self.group][self.pod_group][self.week[i]][str(b)]["Преподаватель"])} | Кабинет - {str(self.nus_classes[self.group][self.pod_group][self.week[i]][str(b)]["Кабинет"])}'+'\n'
                except KeyError:
                    continue
            q +='\n'
        return q



