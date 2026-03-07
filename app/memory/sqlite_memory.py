import sqlite3

DB_PATH = "data/math_memory.db"

def init_memory():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solved_problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        expression TEXT,
        solution TEXT,
        explanation TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_solution(question, parsed_problem, solution):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO solved_problems (question, expression, solution, explanation)
    VALUES (?, ?, ?, ?)
    """, (
        question,
        parsed_problem["expression"],
        solution["symbolic_solution"],
        solution["explanation"]
    ))

    conn.commit()
    conn.close()

def get_past_solutions():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT question, solution FROM solved_problems")

    rows = cursor.fetchall()

    conn.close()

    return rows