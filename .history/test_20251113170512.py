# -------------------------------
# 🧠 Cybersecurity Quiz Program
# Author: João / Sampson
# Description:
# This program uses Object-Oriented Programming (OOP)
# to create and display quiz questions about password safety.
# -------------------------------

# Class representing one possible answer option
class Alternative:
    """
    Represents a possible answer to a question.
    """
    def __init__(self, text, is_correct=False):
        self.text_alternative = text
        self.is_correct = is_correct


# Class representing a question (which contains multiple alternatives)
class Question:
    """
    Represents a gamified question with text and several answer choices.
    """
    def __init__(self, text):
        self.text_question = text
        self.alternatives = []

    def add_alternative(self, alternative):
        """Add an alternative to the question."""
        self.alternatives.append(alternative)

    def __str__(self):
        """Return the question and its alternatives in a readable format."""
        output = f"🤔 Question: {self.text_question}\n"
        labels = ['A', 'B', 'C', 'D']
        for i, alt in enumerate(self.alternatives):
            output += f"   {labels[i]}) {alt.text_alternative}\n"
        return output


# --- Function that creates and displays all quiz challenges ---
def create_and_display_challenges():
    challenges = []

    # 💡 Challenge 1
    q1 = Question("You want to protect your gaming and social media accounts. What is the best way to create your password?")
    q1.add_alternative(Alternative("Use '123456' because it’s quick and easy"))
    q1.add_alternative(Alternative("Use the same password for everything"))
    q1.add_alternative(Alternative("Create a password with letters, numbers, and symbols, and don’t reuse it", is_correct=True))
    challenges.append(q1)

    # 💡 Challenge 2
    q2 = Question("True or False: It’s safe to use the same password on many sites.")
    q2.add_alternative(Alternative("True"))
    q2.add_alternative(Alternative("False", is_correct=True))
    challenges.append(q2)

    # 💡 Challenge 3
    q3 = Question("Choose the best password habit and explain why it helps keep your accounts secure.")
    q3.add_alternative(Alternative("Change your password regularly", is_correct=True))
    q3.add_alternative(Alternative("Write your password on a post-it"))
    q3.add_alternative(Alternative("Share your password only with close friends"))
    challenges.append(q3)

    # 💡 Challenge 4
    q4 = Question("You receive an email asking for your password with a suspicious link. What should you do?")
    q4.add_alternative(Alternative("Reply with your password"))
    q4.add_alternative(Alternative("Ignore and report the email", is_correct=True))
    q4.add_alternative(Alternative("Click the link to check what it says"))
    challenges.append(q4)

    # 💡 Challenge 5
    q5 = Question("You have 20 seconds! Which password is the strongest?")
    q5.add_alternative(Alternative("password123"))
    q5.add_alternative(Alternative("L$8x9#Bq!m", is_correct=True))
    q5.add_alternative(Alternative("myname2025"))
    q5.add_alternative(Alternative("qwerty"))
    challenges.append(q5)

    # 💡 Bonus Challenge (Riddle)
    riddle_text = (
        "I am something you must keep secret. "
        "Made of letters, numbers, and maybe a symbol or two, "
        "I am the key to your account. Without me, no one gets in. What am I?"
    )
    q_bonus = Question(riddle_text)
    q_bonus.add_alternative(Alternative("Username"))
    q_bonus.add_alternative(Alternative("Password", is_correct=True))
    q_bonus.add_alternative(Alternative("Email"))
    challenges.append(q_bonus)

    # Print all challenges
    print("--- Example of Creating and Displaying Question and Alternative Objects ---")
    for idx, q in enumerate(challenges):
        print(f"\n--- Challenge {idx + 1} ---")
        print(q)


# Run the program
if __name__ == "__main__":
    create_and_display_challenges()
