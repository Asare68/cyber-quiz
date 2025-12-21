class Questions :
    def __init__(self, question_text, answer_text):
        self.question = question_text
        self.answer= answer_text

        def check_answer(self, user_answer):
            return user_answer == self.answer
q1 = Questions("Desafio 1: Senhas Secretas (Múltipla Escolha) Você quer proteger suas contas de jogos e redes sociais. Qual opção é a melhor escolha para criar sua senha? ", "Paris")