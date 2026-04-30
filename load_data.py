import csv
from database import get_db

def load_data():
    conn = get_db()
    cursor = conn.cursor()

    with open('cwurData.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            country = row['country']
            institution = row['institution']
            rank = row['world_rank']
            score = row['score']
            year = row['year']

            
            cursor.execute(
                "INSERT OR IGNORE INTO countries (country) VALUES (?)",
                (country,)
            )

            
            cursor.execute(
                "SELECT id FROM countries WHERE country = ?",
                (country,)
            )
            country_id = cursor.fetchone()['id']

            # insert university
            cursor.execute(
                '''INSERT INTO universities
                   (institution, rank, score, year, country_id)
                   VALUES (?, ?, ?, ?, ?)''',
                (institution, rank, score, year, country_id)
            )

    conn.commit()
    conn.close()
    print("Data Loaded Successfully")


if __name__ == '__main__':
    load_data()