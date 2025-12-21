class Alternativa:
    def __init__(self, texto, correta=False):
        self.texto_alternativa = texto
        self.correta = correta


class Pergunta:
    def __init__(self, texto):
        self.texto_pergunta = texto
        self.alternativas = []

    def adicionar_alternativa(self, alternativa):
        self.alternativas.append(alternativa)

    def __str__(self):
        resultado = f"🤔 Aqui vai uma pergunta para você:\n{self.texto_pergunta}\n"
        labels = [chr(i) for i in range(ord('A'), ord('A') + len(self.alternativas))]
        for i, alt in enumerate(self.alternativas):
            resultado += f"   {labels[i]}) {alt.texto_alternativa}\n"
        return resultado

    def verificar_resposta(self, letra):
        labels = [chr(i) for i in range(ord('A'), ord('A') + len(self.alternativas))]
        if letra.upper() in labels:
            indice = labels.index(letra.upper())
            return self.alternativas[indice].correta
        else:
            return False


def criar_quiz():
    quiz = []

    p1 = Pergunta("Você quer proteger suas contas de jogos e redes sociais. Qual a melhor forma de criar sua senha?")
    p1.adicionar_alternativa(Alternativa("Usar '123456' porque é rápido e fácil"))
    p1.adicionar_alternativa(Alternativa("Usar a mesma senha para tudo"))
    p1.adicionar_alternativa(Alternativa("Criar uma senha com letras, números e símbolos, e não reutilizá-la", correta=True))
    quiz.append(p1)

    p2 = Pergunta("Verdadeiro ou falso: É seguro usar a mesma senha em vários sites.")
    p2.adicionar_alternativa(Alternativa("Verdadeiro"))
    p2.adicionar_alternativa(Alternativa("Falso", correta=True))
    quiz.append(p2)

    p3 = Pergunta("Escolha o melhor hábito com senhas e diga por que ele ajuda a proteger sua conta.")
    p3.adicionar_alternativa(Alternativa("Mudar a senha regularmente", correta=True))
    p3.adicionar_alternativa(Alternativa("Anotar a senha em um post-it"))
    p3.adicionar_alternativa(Alternativa("Compartilhar a senha só com amigos próximos"))
    quiz.append(p3)

    p4 = Pergunta("Você recebe um e-mail pedindo sua senha com um link suspeito. O que você faz?")
    p4.adicionar_alternativa(Alternativa("Responder com minha senha"))
    p4.adicionar_alternativa(Alternativa("Ignorar e denunciar o e-mail", correta=True))
    p4.adicionar_alternativa(Alternativa("Clicar no link para ver o que diz"))
    quiz.append(p4)

    p5 = Pergunta("Você tem 20 segundos! Qual dessas senhas você escolheria como a mais forte?")
    p5.adicionar_alternativa(Alternativa("senha123"))
    p5.adicionar_alternativa(Alternativa("L$8x9#Bq!m", correta=True))
    p5.adicionar_alternativa(Alternativa("meunome2025"))
    p5.adicionar_alternativa(Alternativa("qwerty"))
    quiz.append(p5)

    p6 = Pergunta("Qual a melhor forma de lembrar senhas complicadas?")
    p6.adicionar_alternativa(Alternativa("Usar um gerenciador de senhas", correta=True))
    p6.adicionar_alternativa(Alternativa("Anotá-las no papel"))
    p6.adicionar_alternativa(Alternativa("Usar senhas simples"))
    quiz.append(p6)

    # Novas perguntas adicionadas
    p7 = Pergunta("Você está familiarizado com ameaças comuns à cibersegurança, como malware, ransomware e engenharia social?")
    p7.adicionar_alternativa(Alternativa("Sim", correta=True))
    p7.adicionar_alternativa(Alternativa("Não"))
    quiz.append(p7)

    p8 = Pergunta("Você participa de atividades ou questionários de conscientização sobre segurança para se manter informado?")
    p8.adicionar_alternativa(Alternativa("Sim", correta=True))
    p8.adicionar_alternativa(Alternativa("Não"))
    quiz.append(p8)

    p9 = Pergunta("Você revisa e ajusta as configurações de privacidade e segurança nas suas contas de redes sociais?")
    p9.adicionar_alternativa(Alternativa("Sim", correta=True))
    p9.adicionar_alternativa(Alternativa("Não"))
    quiz.append(p9)

    p10 = Pergunta("Você sabe quem pode ver suas postagens e informações pessoais online?")
    p10.adicionar_alternativa(Alternativa("Sim", correta=True))
    p10.adicionar_alternativa(Alternativa("Não"))
    quiz.append(p10)

    # Pergunta bônus com enigma
    enigma_texto = (
        "Sou algo que você deve manter em segredo. "
        "Feito de letras, números e, talvez, símbolos também. "
        "Sou a chave para sua conta — você precisa de mim para entrar. O que sou eu?"
    )
    p_bonus = Pergunta(enigma_texto)
    p_bonus.adicionar_alternativa(Alternativa("Nome de usuário"))
    p_bonus.adicionar_alternativa(Alternativa("Senha", correta=True))
    p_bonus.adicionar_alternativa(Alternativa("Email"))
    quiz.append(p_bonus)

    return quiz


def executar_quiz():
    quiz = criar_quiz()
    pontos = 0

    print("🌟 Bem-vindo ao seu amigável Quiz de Segurança Cibernética! Vamos testar seus conhecimentos.\n")
    print("Digite a letra da sua resposta e pressione Enter.\n")

    for i, pergunta in enumerate(quiz, 1):
        print(f"Pergunta {i} de {len(quiz)}:")
        print(pergunta)

        opcoes_validas = [chr(j) for j in range(ord('A'), ord('A') + len(pergunta.alternativas))]

        while True:
            resposta = input("Sua resposta (A, B, C, ...): ").strip().upper()
            if resposta in opcoes_validas:
                if pergunta.verificar_resposta(resposta):
                    print("🎉 Muito bem! Resposta correta!\n")
                    pontos += 1
                else:
                    print("😕 Quase lá! Continue aprendendo e você vai conseguir!\n")
                break
            else:
                print(f"Ops! Por favor, digite uma das seguintes letras: {', '.join(opcoes_validas)}")

    print(f"Você arrasou! Sua pontuação final foi {pontos} de {len(quiz)}. Mantenha-se seguro online! 🔐")


if __name__ == "__main__":
    executar_quiz()
