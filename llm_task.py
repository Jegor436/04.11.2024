from transformers import pipeline

def generate_questions(topic, num_questions=3):
    generator = pipeline('text-generation', model='gpt2')

    prompt = f"Generate {num_questions} different questions about {topic}:\n1."

    result = generator(
        prompt,
        max_length=150,
        do_sample=True,
        temperature=0.6,
        top_k=50,
        top_p=0.95,
        num_return_sequences=3
    )

    all_texts = [r['generated_text'][len(prompt):].strip() for r in result]

    questions_set = set()
    for text in all_texts:
        lines = text.replace("2.", "\n2.").replace("3.", "\n3.").split("\n")
        for line in lines:
            line = line.strip()
            if line and line not in questions_set:
                questions_set.add(line)
            if len(questions_set) >= num_questions:
                break
        if len(questions_set) >= num_questions:
            break

    return "\n".join(list(questions_set)[:num_questions])

def main():
    print("AI Question Generator")
    topic = input("Enter topic: ").strip()

    if topic:
        print(f"\nQuestions about: {topic}\n")
        questions = generate_questions(topic)
        print(questions)
    else:
        print("No topic entered.")

if __name__ == "__main__":
    main()