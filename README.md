## Курсовая 5. Работа с базами данных 
Проект предназначен для получения данных о компаниях и вакансиях с сайта hh.ru,
проектирования таблиц в БД PostgreSQL, загрузки полученных данных в созданные таблицы
и получения информации из созданных таблиц по определенным шаблонам.


## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)

## Технологии
- [Python 3.11.4](https://www.python.org/)

## Начало работы
Клонировать проект с репозитория. Настройки проекта хранятся в файле config.py.
В поле "company_ids" можно задать id компаний, которые интересуют пользователя.
Поле "only_with_salary" отвечает за отображение вакансий с зарплатой или без зарплаты
(True - показывать вакансии только с зп, False - показывать все вакансии).
В поле "vacancies_per_page" задается количество вакансий, которые будут предоставлены пользователю.
Поле "area" задает регион для поиска вакансий. По умолочанию поиск идет по России.
Также в Pycharm необходимо создать переменную окружения 'PWD', содержащую пароль.

После завершения подготовки необходимо запустить файл main.py. При этом произойдет заполнение таблиц
работодателей и вакансий. После этого с таблицами можно осуществить следующие действия:
- Вывести список компаний и количество вакансий в каждой из компаний
- Вывести список компаний, вакансий, минимальную/макмимальную зарплаты и ссылку на вакансию
- Вывести среднюю зарплату
- Вывести список вакансий с зарплатой выше средней
- Вывести список вакансий по ключевому слову

Для завершения работы программы необходимо ввести команду "stop".





