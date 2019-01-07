import vk # импортируем модуль vk


def get_members(groupid): # функция формирования базы участников сообщества в виде списка
    first = vk_api.groups.getMembers(group_id=groupid, v=5.92) # первое выполнение метода
    data = first["items"] # присваиваем переменной первую тысячу id'шников
    count = first["count"] // 1000 # присваиваем переменной количество тысяч участников
    for i in range(1, count+1): # с каждым проходом цикла смещение offset увеличивается на тысячу и еще тысяча id'шников добавляется к нашему списку
        data = data + vk_api.groups.getMembers(group_id=groupid, v=5.92, offset=i*1000)["items"]
    return data


def save_data(data, filename="data"): # функция сохранения базы в txt файле
    file = open(str(filename) +".txt", "w") # открываем файл на запись
    for item in data: # записываем каждый id'шник в новой строке, добавляя в начало "vk.com/id", а в конец перенос строки
        file.write("vk.com/id" + str(item) + "\n") 
    file.close() # закрываем файл


def enter_data(filename="data"): # функция ввода базы из txt файла
    file = open(str(filename)+".txt") # открываем файл на чтение
    b = [] # создаем пустой список
    for line in file: # записываем каждую строчку файла в список, убирая "vk.com/id" и "\n" с помощью среза
        b.append(line[9:len(line) - 1])
    file.close() # закрываем файл
    return b
    
    
def get_intersection(group1, group2): # функция нахождения пересечений двух баз
    all_members = len(group1) + len(group2) # для удобства сохраняем сумму участников двух сообществ
    group1 = set(group1) # делаем множество из списка участников первой группы
    group2 = set(group2) # делаем множество из списка участников второй группы
    intersection = group1.intersection(group2) # находим пересечение двух множеств
    all_members = all_members - len(intersection) # убираем из суммы участников повторы
    result = len(intersection)/all_members * 100 # высчитываем пересечение в процентах
    print("Пересечение аудиторий: ", round(result,2), "%", sep="") # выводим результат, округляя его до 2 цифр после запятой
    return list(intersection) # возвращаем список


def union_members(group1, group2): # функция объединения двух баз без повторов
    group1 = set(group1) # делаем множество из списка участников первой группы
    group2 = set(group2) # делаем множество из списка участников второй группы
    unity = group1.union(group2) # объединяем два множества
    return list(unity) # возвращаем список


if __name__ == "__main__": 
    token = ""  # сервисный ключ доступа
    session = vk.Session(access_token=token) # авторизация
    vk_api = vk.API(session)
