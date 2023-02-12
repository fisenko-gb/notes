import json
from datetime import datetime

BASE_FILE = 'data.json'
data_from_json = []

def read_base():
    global data_from_json
    try:
        with open(BASE_FILE, 'r', encoding='UTF-8') as f_o:
            data_from_json = json.load(f_o)
            return data_from_json
    except Exception as err:
        print(f'Ошибка {err.__class__} {err}')
        data_from_json = []
        write_base()
        return data_from_json


def write_base():
    global data_from_json
    string_json = json.dumps(data_from_json, indent=4, ensure_ascii=False)
    with open(BASE_FILE, 'w', encoding='UTF-8') as f_o:
        f_o.write(string_json)


def show_tuple_string(t_tuple):
    rez_string = ''
    for i in t_tuple:
        for key, value in i.items():
            rez_string += str(value) + '\n'
        rez_string += '\n'
    return rez_string


def delete_str_base(t_id: int):
    global data_from_json
    data_from_json = read_base()
    for i, j in enumerate(data_from_json):
        if j['id'] == t_id:
            del data_from_json[i]
            break
    write_base()


def update_str_base(new_str):
    global data_from_json
    data_from_json = read_base()
    for i in data_from_json:
        if i['id'] == new_str['id']:
            i['heading'] = new_str['heading']
            i['body'] = new_str['body']
            i['note_date'] = datetime.now()
            break
    write_base()


def search_base(str_searh: str) -> list:
    global data_from_json
    rez = []
    data_from_json = read_base()
    for i in data_from_json:
        for val in i.values():
            if type(val) == int:
                continue
            if str_searh.lower() in val.lower():
                rez.append(i)
                break

    return rez


def add_base(heading: str, body: str):
    global data_from_json
    data_from_json = read_base()
    try:
        last_index = data_from_json[len(data_from_json) - 1]
        id = int(last_index['id']) + 1
    except:
        id = 1
    t_date = str(datetime.now())
    data_from_json.append({'id': id, 'heading': heading, 'body': body, 'note_date': t_date})
    write_base()

##################################################################################################
##################################################################################################

def test_read_and_write():
    global data_from_json
    data_from_json = read_base()
    print(data_from_json)
    print(show_tuple_string(data_from_json))
    add_base('Заметка1', 'Текст заметки 1')
    add_base('Заметка2', 'Текст заметки 2')
    add_base('Заметка3', 'Текст заметки 3')
    add_base('Заметка4', 'Текст заметки 4')
    add_base('Заметка5', 'Текст заметки 5')
    print(data_from_json)
    print(show_tuple_string(data_from_json))

def test_sear(t_str: str):
    rez_searh = search_base(t_str)
    print(show_tuple_string(rez_searh))


# test_read_and_write()
#test_sear('ива')
