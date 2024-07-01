import sqlite3


def get_connection():
    conn = sqlite3.connect('gym.db')
    return conn


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            id TEXT PRIMARY KEY,
            name TEXT,
            contact TEXT,
            join_date TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            member_id TEXT,
            date TEXT,
            FOREIGN KEY(member_id) REFERENCES Members(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Fees (
            member_id TEXT,
            due_date TEXT,
            FOREIGN KEY(member_id) REFERENCES Members(id)
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    setup_database()
