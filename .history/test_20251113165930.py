# Definindo a classe Alternativa
# Esta classe representa uma possível resposta ou opção de escolha para uma Questão.
class Alternativa:
    """
    Representa uma alternativa de resposta.
    """
    def __init__(self, texto, e_correta=False):
        # O campo 'texto_alternativa' armazena o conteúdo da opção de resposta [1].
        self.texto_alternativa = texto 
        self.e_correta = e_correta

# Definindo a classe Questao
# Esta classe representa uma pergunta e contém múltiplas Alternativas.
class Questao:
    """
    Representa uma pergunta gamificada, contendo texto e uma lista de alternativas.
    """
    def __init__(self, texto):
        # O campo 'texto_questao' armazena o conteúdo da pergunta [1].
        self.texto_questao = texto
        self.alternativas = [] # Uma questao pode ter varias alternativas [1].

    def adicionar_alternativa(self, alternativa):
        self.alternativas.append(alternativa)

    def __str__(self):
        """Método para exibir a questão e suas alternativas."""
        output = f"🤔 Questão: {self.texto_questao} [1]\n"
        # Usando um índice para apresentar as alternativas: A, B, C, etc.
        rotulos = ['A', 'B', 'C', 'D']
        for i, alt in enumerate(self.alternativas):
            # Exibe o texto da alternativa [1]
            output += f"   {rotulos[i]}) {alt.texto_alternativa}\n"
        return output

# --- Classe Principal de Demonstração (Instanciação de Objetos) ---

def criar_e_exibir_desafios():
    """
    Instancia objetos das classes Questao e Alternativa usando os desafios fornecidos.
    """
    desafios = []

    # 💡 Desafio 1: Senhas Secretas (Múltipla Escolha) [2]
q1 = Questao("Você quer proteger suas contas de jogos e redes sociais. Qual opção é a melhor escolha para criar sua senha?")

q1.adicionar_alternativa(Alternativa("Use '123456' porque é rápido e ninguém vai adivinhar")) [2]
    q1.adicionar_alternativa(Alternativa("Use a mesma senha para tudo para evitar esquecer")) [2]
    q1.adicionar_alternativa(Alternativa("Crie uma senha com letras, números e símbolos, e não a reutilize em outras contas", e_correta=True)) [2]
    desafios.append(q1)

    
    # O modelo Questao/Alternativa é aplicado a Verdadeiro/Falso
    q2 = Questao("Verdadeiro ou Falso: É seguro usar a mesma senha em vários sites.") [2]
    q2.adicionar_alternativa(Alternativa("Verdadeiro"))
    q2.adicionar_alternativa(Alternativa("Falso", e_correta=True)) [2]
    desafios.append(q2)

# Desafio 3: Escolhas Seguras (Múltipla Escolha com Explicação) [3]
    q3 = Questao("Escolha o melhor hábito de senha e explique por que ele ajuda a manter suas contas seguras.") [3]
    q3.adicionar_alternativa(Alternativa("Mude sua senha regularmente", e_correta=True)) [3]
    q3.adicionar_alternativa(Alternativa("Escreva sua senha em um post-it")) [3]
    q3.adicionar_alternativa(Alternativa("Compartilhe sua senha apenas com amigos próximos")) [3]
    desafios.append(q3)

    # 🚨 Desafio 4: Alerta de Phishing! (Contexto) [3]
    q4 = Questao("Você recebe um e-mail pedindo a senha da sua conta com um link suspeito. O que você deve fazer?") [3]
    q4.adicionar_alternativa(Alternativa("Responder com sua senha")) [3]
    q4.adicionar_alternativa(Alternativa("Ignorar e denunciar o e-mail", e_correta=True)) [3]
    q4.adicionar_alternativa(Alternativa("Clicar no link para ver o que diz")) [3]
    desafios.append(q4)

    # ⚡ Desafio 5: Rodada Rápida (Desafio do Cronômetro) [4]
    q5 = Questao("Você tem 20 segundos! Qual é a senha mais forte?") [4]
    q5.adicionar_alternativa(Alternativa("password123")) [4]
    q5.adicionar_alternativa(Alternativa("L$8x9#Bq!m", e_correta=True)) [4]
    q5.adicionar_alternativa(Alternativa("myname2025")) [4]
    q5.adicionar_alternativa(Alternativa("qwerty")) [4]
    desafios.append(q5)


    # ❓ Desafio Bônus: Enigma da Senha [4]
    # Modelado como Questão com alternativas para encaixar na estrutura POO
    riddle_text = "Sou algo que você deve manter em segredo. Feito de letras, números, um ou dois símbolos, sou a chave da sua conta. Sem mim, ninguém passa. O que sou eu?" [4]
    q_bonus = Questao(riddle_text)
    q_bonus.adicionar_alternativa(Alternativa("Nome de usuário"))
    q_bonus.adicionar_alternativa(Alternativa("Senha", e_correta=True))
    q_bonus.adicionar_alternativa(Alternativa("E-mail"))
    desafios.append(q_bonus)
    
    print("--- Exemplo de Instanciação e Exibição de Objetos de Questão e Alternativa ---")
    
    # Iterar sobre os desafios e exibi-los
    for idx, q in enumerate(desafios):
        print(f"\n--- Desafio {idx + 1} ---")
        print(q)

if __name__ == "__main__":
    criar_e_exibir_desafios()#Greet the user