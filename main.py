import json_worker as js

message_hi = 'Добро пожаловать в программу заметки!\n '
message_bay = 'До скорых встреч!'

message_level1 = 'Вот какие действия Вам доступны:\n' \
                '1 - Показать все заметки\n' \
                '2 - Новая заметка\n' \
                '3 - Найти заметку\n' \
                '4 - Выход\n' \
                'введите цифру с необходимым действием: '

message_level2 = 'Вот какие действия Вам доступны:\n' \
                '1 - Выбрать заметку\n' \
                '2 - Назад\n' \
                'введите цифру с необходимым действием: '

message_level3 = 'Вот какие действия Вам доступны:\n' \
                '1 - Редактировать заметку\n' \
                '2 - Удалить заметку\n' \
                '3 - Назад\n' \
                'введите цифру с необходимым действием: '

def start():
    print(message_hi)
    while True:
        answer = input(message_level1).strip()
        if answer == '1':
            js.print_all()
            print()
        elif answer == '2':
            haeding = input('Введите заголовок заметки: ').strip()
            body = input('Введите текст заметки: ').strip()
            js.add_base(haeding, body)
            print('Заметка успешна сохранена\n')
        elif answer == '3':
            t_str = ''
            str_search = input('\nВведите строку поиска: ').strip()
            rez_searh = js.search_base(str_search)
            if len(rez_searh) > 0:
                print(js.show_tuple_string(rez_searh))
                answer = input(message_level2).strip()
                if answer == '1':
                    answer_id = input('Введите порядковый номер заметки: ').strip()
                    for i in rez_searh:
                        if str(i['id']) == answer_id:
                            t_str = i
                            break
                    if not t_str == '':
                        answer = input(message_level3).strip()
                        if answer == '1':
                            i['heading'] = input('Введите заголовок заметки: ').strip()
                            i['body'] = input('Введите текст заметки: ').strip()
                            js.update_str_base(i)
                            print('Заметка успешна сохранена\n')
                        elif answer == '2':
                            js.delete_str_base(i['id'])
                            print('\nЗаметка удалена...')
                    else:
                        print('Не найдена строка с введенным номером...\n')
            else:
                print('Ничего не найдено...\n')
        elif answer == '4':
            break;
        else:
            print('Вводить можно только цифры, указанные в меню...')


    print(message_bay)

if __name__ == '__main__':
    start()

