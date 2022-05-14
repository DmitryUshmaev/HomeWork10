import json

# Функция для чтения json файла
def open_json(json_file):
    with open(json_file, encoding='utf-8') as f:
        json_f = json.load(f)
    return json_f

# Возвращает список с шаблоном со всеми кандидатами
def candidates_home(json_file):
    candidates = []
    for i in json_file:
        candidates.append(f'<pre>Имя кандидата - {i["name"]}\nПозиция кандидата {i["position"]}\nНавыки: {i["skills"]}</pre>')
    return candidates

# Возвращает список с шаблоном и с картинками кандидатов
def candidates_profile(json_file):
    candidate_profile = []
    for i in json_file:
        candidate_profile.append(f'<img src="{i["picture"]}">\n<pre>Имя кандидата - {i["name"]}\nПозиция кандидата {i["position"]}\nНавыки: {i["skills"]}</pre>')
    return candidate_profile

# Возвращает список кандидатов
def candidates_skills(json_file):
    candidate = []
    for i in json_file:
        candidate.append(i)
    return candidate
