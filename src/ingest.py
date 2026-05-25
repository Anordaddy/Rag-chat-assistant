import sys
from pypdf import PdfReader
from pgvector.psycopg2 import register_vector

from chunker import chunk_text
from embedder import get_embedding
from db import get_connection

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <pdf_path>")
        return

    pdf_path = sys.argv[1]

    print("Loading PDF...")
    text = extract_text(pdf_path)

    print("Chunking text...")
    chunks = chunk_text(text)

    conn = get_connection()
    register_vector(conn)

    cur = conn.cursor()

    print("Embedding and storing chunks...")

    for chunk in chunks:
        embedding = get_embedding(chunk)

        cur.execute(
            """
            INSERT INTO chunks (text, embedding, source)
            VALUES (%s, %s, %s)
            """,
            (chunk, embedding, pdf_path)
        )

    conn.commit()

    cur.close()
    conn.close()

    print(f"Done. {len(chunks)} chunks stored.")

if __name__ == "__main__":
    main()