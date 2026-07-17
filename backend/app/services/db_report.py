from app.services.database import get_connection


def save_to_database(filename, analysis):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reports
        (filename, score, grade, summary)
        VALUES (?, ?, ?, ?)
    """, (
        filename,
        analysis["score"],
        analysis["grade"],
        analysis["summary"]
    ))

    conn.commit()
    conn.close()