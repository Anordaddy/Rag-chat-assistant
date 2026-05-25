from embedder import get_embedding
from retriever import retrieve_chunks
from generator import generate_answer

def main():
    print("Ready. Ask your questions (type 'exit' to quit).")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Goodbye.")
            break

        question_embedding = get_embedding(question)

        chunks = retrieve_chunks(question_embedding)

        answer = generate_answer(question, chunks)

        print(f"\nAssistant: {answer}")

if __name__ == "__main__":
    main()