import json
# import candidates.json


FILE_DIR = 'candidates.json'

def load_candidates(FILE_DIR): # которая загрузит данные из файла
    with open(FILE_DIR, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def get_all():
    data = load_candidates(FILE_DIR)
    result = ''
    for i in data:
        result += '\n'
        result += i["name"] + '\n'
        result += i["position"] + '\n'
        result += i["skills"] + '\n'
    return (f'<pre> {result} </pre>')


def et_by_pk(pk): # которая вернет кандидата по pk
    data = load_candidates(FILE_DIR)
    candidate = ''

    for i in data:
        if i['pk'] == pk:
            picture = (f'<img src = {i["picture"]}>')
            candidate += i["name"] + '\n'
            candidate += i["position"] + '\n'
            candidate += i["skills"] + '\n'
            return (picture + f'<pre> {candidate} </pre>')
    return ('Кандидат не найден')


def get_by_skill(skill_name): # которая вернет кандидатов по навыку
    data = load_candidates(FILE_DIR)
    candidate_list = ''
    for i in data:
        if skill_name in i['skills'].lower():
            candidate_list += i['name'] + '\n'
    return (f'<pre> {candidate_list} </pre>')

