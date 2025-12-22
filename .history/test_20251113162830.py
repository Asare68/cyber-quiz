class Questions :
    def __init__(self, question_text, answer_text):
        self.question = question_text
        self.answer= answer_text

        def check_answer(self, user_answer):
            return user_answer == self.answer