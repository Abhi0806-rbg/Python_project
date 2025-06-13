def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i].startswith('#') and i + 6 < len(lines):
            question_text = lines[i+1]
            options = [lines[i+2], lines[i+3], lines[i+4], lines[i+5]]
            answer_line = lines[i+6]
            try:
                correct_option = int(answer_line.split(':')[1])
            except (IndexError, ValueError):
                print(f"Invalid answer format at question {lines[i]}")
                i += 7
                continue

            questions.append({
                "question": question_text,
                "options": options,
                "answer": correct_option
            })
            i += 7
        else:
            i += 1
    return questions

def start_quiz(questions):
    correct = 0

    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {q['question']}")
        for i, opt in enumerate(q['options'], 1):
            print(f"{i}. {opt}")
        try:
            user_input = int(input("Your Answer (1-4): "))
            if user_input == q['answer']:
                print(" Correct!")
                correct += 1
            else:
                print(f" Wrong! Correct Answer: {q['answer']}. {q['options'][q['answer'] - 1]}")
        except ValueError:
            print("⚠ Invalid input! Treated as wrong.")

    total = len(questions)
    wrong = total - correct
    percentage = (correct / total) * 100
    result = "PASS" if percentage >= 40 else "FAIL"

    print("\n Quiz Summary:")
    print(f" Correct Answers: {correct}")
    print(f" Wrong Answers: {wrong}")
    print(f" Percentage: {percentage:.2f}%")
    print(f" Result: {result}")

# Main Execution
if __name__ == "__main__":
    quiz_questions = load_questions("que_quiz.txt")
    if quiz_questions:
        start_quiz(quiz_questions)
    else:
        print("No valid questions loaded.")
