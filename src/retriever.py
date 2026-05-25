from db import get_connection
from config import TOP_K

def retrieve_chunks(question_embedding):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT text
    FROM chunks
    ORDER BY embedding <=> %s::vector
    LIMIT %s;
    """

    cur.execute(query, (question_embedding, TOP_K))

    results = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in results]