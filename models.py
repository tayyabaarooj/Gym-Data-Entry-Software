import uuid
from datetime import datetime, timedelta
from database import get_connection


def register_member(name, contact):
    member_id = str(uuid.uuid4())
    join_date = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Members (id, name, contact, join_date) VALUES (?, ?, ?, ?)",
                   (member_id, name, contact, join_date))

    due_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO Fees (member_id, due_date) VALUES (?, ?)", (member_id, due_date))

    conn.commit()
    conn.close()
    return member_id


def mark_attendance(member_id):
    date = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Attendance (member_id, date) VALUES (?, ?)", (member_id, date))
    conn.commit()
    conn.close()


def check_due_fees():
    today = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Members.name, Fees.due_date FROM Fees INNER JOIN Members ON Fees.member_id = Members.id WHERE due_date <= ?",
        (today,))
    due_fees = cursor.fetchall()
    conn.close()

    return due_fees


def update_fee_due_date(member_id):
    next_due_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Fees SET due_date = ? WHERE member_id = ?", (next_due_date, member_id))
    conn.commit()
    conn.close()
