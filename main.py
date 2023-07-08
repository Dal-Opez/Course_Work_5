import os
from db_manager import DBManager
from utils import insert_vacancy_data_to_db, insert_employer_data_to_db
from hh_engine_class import HHApi

db = DBManager(
    dbname="coursework",
    user="postgres",
    password=os.environ['PWD'],
    host="localhost",
    port="5432",
)
def main():

    hh = HHApi()
    # print(hh.get_employers_data())
    # print(hh.get_vacancies())

    db = DBManager(
        dbname="coursework",
        user="postgres",
        password=os.environ['PWD'],
        host="localhost",
        port="5432",
    )

    db.drop_tables()
    db.create_tables()

    insert_employer_data_to_db(hh.get_employers_data(), db)
    insert_vacancy_data_to_db(hh.get_vacancies(), db)


    print("Привет! Выберите один из предложенных вариантов действий:")
    while 1:
        print("""
        1 - Вывести список компаний и количество вакансий в каждой из компаний
        2 - Вывести список компаний, вакансий, минимальную/макмимальную зарплаты и ссылку на вакансию
        3 - Вывести среднюю зарплату
        4 - Вывести список вакансий с зарплатой выше средней
        5 - Вывести список вакансий по ключевому слову
        stop - Завершение работы программы\n""")

        user_input = input("Ваш выбор:").lower()

        if user_input == '1':
            for item in db.get_companies_and_vacancies_count():
               print(item)
        elif user_input == '2':
            for item in db.get_all_vacansies():
               print(item)
        elif user_input == '3':
           print(db.get_avg_salary())
        elif user_input == '4':
            for item in db.get_vacansies_with_higher_salary():
               print(item)
        elif user_input == '5':
            user_input = input("Введите keyword: ")
            for item in db.get_vacancies_with_keyword(user_input):
               print(item)
        elif user_input == 'stop':
            print("До новых встреч!")
            break
        else:
            print("Некорректный ввод!")



if __name__ == '__main__':
    main()