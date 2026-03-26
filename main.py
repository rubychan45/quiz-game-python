# ============================================
#         PYTHON QUIZ GAME
#         Beginner Project - BCA Data Science
# ============================================

# --- QUESTIONS, OPTIONS, AND ANSWERS ---
# Each question is stored as a dictionary (like a box holding related info)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["A. Java", "B. HTML", "C. Python", "D. CSS"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Computer Personal Unit", "C. Central Processing Unit", "D. Core Processing Unit"],
        "answer": "C"
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["A. 365", "B. 364", "C. 366", "D. 367"],
        "answer": "C"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. Integer", "B. Slide", "C. Column", "D. Sheet"],
        "answer": "A"
    }
]

# ============================================
#               GAME STARTS HERE
# ============================================

# Print a welcome banner
print("=" * 45)
print("        WELCOME TO THE QUIZ GAME!")
print("=" * 45)

# Ask for the player's name
name = input("\nEnter your name: ")
print(f"\nHello {name}! Let's begin the quiz.")
print("Type A, B, C, or D to answer each question.\n")
print("-" * 45)

# Variable to track the score
score = 0

# Loop through each question one by one
for i, q in enumerate(questions):

    # Show question number and question text
    print(f"\nQuestion {i + 1}: {q['question']}")

    # Show all 4 options
    for option in q["options"]:
        print(option)

    # Take the player's answer and convert to uppercase (so 'b' = 'B')
    user_answer = input("\nYour answer: ").strip().upper()

    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1          # Add 1 point for correct answer
    else:
        print(f"Wrong! The correct answer was: {q['answer']}")

    print("-" * 45)

# ============================================
#               FINAL SCORE
# ============================================

print(f"\nQuiz Over! Well done, {name}!")
print(f"Your Score: {score} out of {len(questions)}")

# Give a message based on score
if score == len(questions):
    print("Result: PERFECT SCORE! Outstanding!")
elif score >= 3:
    print("Result: Great job! Keep it up!")
elif score >= 2:
    print("Result: Good effort! Practice more.")
else:
    print("Result: Keep trying! You'll get better.")

print("=" * 45)
