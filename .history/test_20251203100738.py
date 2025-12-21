# -------------------------------
# 🧠 Friendly Cybersecurity Quiz Program
# Author: Sampson (humanized)
# -------------------------------

class Alternative:
    def __init__(self, text, is_correct=False):
        self.text_alternative = text
        self.is_correct = is_correct

class Question:
    def __init__(self, text):
        self.text_question = text
        self.alternatives = []

    def add_alternative(self, alternative):
        self.alternatives.append(alternative)

    def __str__(self):
        output = f"🤔 Here’s a question for you:\n{self.text_question}\n"
        labels = [chr(i) for i in range(ord('A'), ord('A') + len(self.alternatives))]
        for i, alt in enumerate(self.alternatives):
            output += f"   {labels[i]}) {alt.text_alternative}\n"
        return output

    def check_answer(self, answer_label):
        labels = [chr(i) for i in range(ord('A'), ord('A') + len(self.alternatives))]
        if answer_label.upper() in labels:
            index = labels.index(answer_label.upper())
            return self.alternatives[index].is_correct
        else:
            return False

def create_quiz():
    quiz = []

    q1 = Question("You want to protect your gaming and social media accounts. What’s the best way to create your password?")
    q1.add_alternative(Alternative("Use '123456' because it’s quick and easy"))
    q1.add_alternative(Alternative("Use the same password for everything"))
    q1.add_alternative(Alternative("Create a password with letters, numbers, and symbols, and don’t reuse it", is_correct=True))
    quiz.append(q1)

    q2 = Question("True or False: It’s safe to use the same password on many sites.")
    q2.add_alternative(Alternative("True"))
    q2.add_alternative(Alternative("False", is_correct=True))
    quiz.append(q2)

    q3 = Question("Choose the best password habit and tell us why it helps keep your accounts safe.")
    q3.add_alternative(Alternative("Change your password regularly", is_correct=True))
    q3.add_alternative(Alternative("Write your password on a post-it"))
    q3.add_alternative(Alternative("Share your password only with close friends"))
    quiz.append(q3)

    q4 = Question("You get an email asking for your password with a suspicious link. What’s your move?")
    q4.add_alternative(Alternative("Reply with your password"))
    q4.add_alternative(Alternative("Ignore and report the email", is_correct=True))
    q4.add_alternative(Alternative("Click the link to see what it says"))
    quiz.append(q4)

    q5 = Question("You have 20 seconds! Which password would you pick as the strongest?")
    q5.add_alternative(Alternative("password123"))
    q5.add_alternative(Alternative("L$8x9#Bq!m", is_correct=True))
    q5.add_alternative(Alternative("myname2025"))
    q5.add_alternative(Alternative("qwerty"))
    quiz.append(q5)

    q6

    riddle_text = (
        "I’m something you must keep secret. "
        "Made of letters, numbers, maybe symbols too. "
        "I’m the key to your account—you need me to get in. What am I?"
    )
    q_bonus = Question(riddle_text)
    q_bonus.add_alternative(Alternative("Username"))
    q_bonus.add_alternative(Alternative("Password", is_correct=True))
    q_bonus.add_alternative(Alternative("Email"))
    quiz.append(q_bonus)

    return quiz

def run_quiz():
    quiz = create_quiz()
    score = 0

    print("🌟 Welcome to your friendly Cybersecurity Quiz! Let's test your knowledge.\n")
    print("Type the letter of your answer and press Enter.\n")

    for i, question in enumerate(quiz, 1):
        print(f"Question {i} of {len(quiz)}:")
        print(question)

        valid_labels = [chr(j) for j in range(ord('A'), ord('A') + len(question.alternatives))]

        while True:
            answer = input("Your answer (A, B, C, ...): ").strip().upper()
            if answer in valid_labels:
                if question.check_answer(answer):
                    print("🎉 Well done! That’s correct!\n")
                    score += 1
                else:
                    print("😕 Not quite right. Keep learning and you'll get it next time!\n")
                break
            else:
                print(f"Oops! Please enter one of: {', '.join(valid_labels)}")

    print(f"You rocked it! Your final score is {score} out of {len(quiz)}. Stay safe online! 🔐")

if __name__ == "__main__":
    run_quiz()
