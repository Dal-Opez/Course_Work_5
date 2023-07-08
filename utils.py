from db_manager import DBManager


def insert_vacancy_data_to_db(data, db):
    with db.conn.cursor() as cur:
        for vacancy in data:
            cur.execute("""
                INSERT INTO vacancies (id, name, company_id, salary_min, salary_max, url)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                vacancy["id"],
                vacancy["name"],
                vacancy["employer"]["id"],
                vacancy["salary"]["from"] if vacancy["salary"]["from"] is not None else 0,
                vacancy["salary"]["to"] if vacancy["salary"]["to"] is not None else 0,
                vacancy["url"]
            ))
            db.conn.commit()

def insert_employer_data_to_db(data, db):
    with db.conn.cursor() as cur:
        for employer in data:
            cur.execute("""
                INSERT INTO companies (id, name, url)
                VALUES (%s, %s, %s)
            """, (
                employer["id"],
                employer["name"],
                employer["url"]
            ))
            db.conn.commit()