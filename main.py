from utils import candidates_home, open_json, candidates_profile, candidates_skills
from flask import Flask


def main():
    app = Flask(__name__)

    # Создаем главную страницу, выводим весь список
    @app.route('/')
    def home_page():
        return "".join(candidates_home(open_json('candidates.json')))

    # Выводим одного кандидата по индексу
    @app.route('/candidate/<int:x>')
    def candidate_page(x):
        return candidates_profile(open_json('candidates.json'))[x]

    # Выводит кандидатов с нужными навыками
    @app.route('/skills/<x>')
    def candidate_skills(x):
        candidate = []
        for i in candidates_skills(open_json('candidates.json')):
            if x.lower() in i['skills'.lower()].split(', '):
                candidate.append(
                    f'<pre>Имя кандидата - {i["name"]}\nПозиция кандидата {i["position"]}\nНавыки: {i["skills"]}</pre>')
        return "".join(candidate)

    app.run()


if __name__ == '__main__':
    main()
