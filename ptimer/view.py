def contact_to_s():
    return input('Введите информацию для поиска ')

def choose_mode():
    return input('Введите режим работ(1-добавление,2-поиск,3-редактирование,4-удаление)')

def new_contact():
    name=input('Введите имя: ')
    phone_num=input('Введите номер: ')
    return f'{name} || {phone_num}'

def show_found(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)

def employee_to_s():
    return input('Введите информацию для поиска: ')

def new_employee():
    name=input('Введите имя: ')
    post=input('Введите должность : ')
    salary=input('Введите зарплату : ')
    phone_num=input('Введите номер: ')
    return f'{name} || {post} || {salary} || {phone_num}'

def clarification():
    return input('Введите id: ')

def error():
    print('Введено некорректное значение ')                