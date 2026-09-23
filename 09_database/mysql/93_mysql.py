"""
Topic: Python + MySQL
Level: Intermediate
Source Reference: W3Schools Python Tutorial (curriculum order only, content is original)
Covers: connection, create, read, update, delete, error handling, parameterized queries.
Install with: pip install mysql-connector-python
Credentials are read from environment variables - never hard-code them.
"""
import os

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "python_learning"),
}

def get_connection():
    """Create and return a MySQL connection using environment-based credentials."""
    import mysql.connector
    return mysql.connector.connect(**DB_CONFIG)


def create_table():
    """CREATE TABLE example (run once)."""
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        score INT NOT NULL
    )
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


def insert_student(name, score):
    """CREATE - insert a row using a parameterized query (prevents SQL injection)."""
    query = "INSERT INTO students (name, score) VALUES (%s, %s)"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (name, score))
        conn.commit()


def get_students():
    """READ - fetch all rows."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, score FROM students")
        return cursor.fetchall()


def update_score(student_id, new_score):
    """UPDATE - modify a row by id, using a parameterized query."""
    query = "UPDATE students SET score = %s WHERE id = %s"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (new_score, student_id))
        conn.commit()


def delete_student(student_id):
    """DELETE - remove a row by id."""
    query = "DELETE FROM students WHERE id = %s"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (student_id,))
        conn.commit()


if __name__ == "__main__":
    try:
        create_table()
        insert_student("Wulan", 88)
        print(get_students())
    except ImportError:
        print("Install mysql-connector-python to run this file for real: "
              "pip install mysql-connector-python")
    except Exception as exc:  # noqa: BLE001 - top-level demo guard
        print(f"Could not connect to MySQL (this is expected without a real DB): {exc}")

# ============================================
# PRACTICE
# ============================================
# EASY 1: Add a `delete_by_score_below(threshold)` function.
# EASY 2: Add an `email` column and update insert_student to accept it.
# EASY 3: Write a function to check whether a student with a given name exists.
# MEDIUM 1: Wrap every function with proper try/except mysql.connector.Error handling.
# MEDIUM 2: Add a function that returns the class average score using SQL AVG().
#
# CHALLENGE: Build a small CLI (using input()) that lets a user add, view,
# update, and delete students via these functions.

# ============================================
# SUMMARY
# ============================================
# Always use parameterized queries (%s placeholders) and environment
# variables for credentials - never string-format SQL or hard-code passwords.
