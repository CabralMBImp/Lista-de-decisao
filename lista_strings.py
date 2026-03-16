import random

# =======================================================
# LISTA DE EXERCÍCIOS - STRINGS
# =======================================================

def ex01():
    print("--- 1. Tamanho de strings ---")
    str1 = input("String 1: ")
    str2 = input("String 2: ")
    print(f"Tamanho de '{str1}': {len(str1)} caracteres")
    print(f"Tamanho de '{str2}': {len(str2)} caracteres")
    print("As duas strings são de tamanhos", "iguais." if len(str1) == len(str2) else "diferentes.")
    print("As duas strings possuem conteúdo", "igual." if str1 == str2 else "diferente.")

def ex02():
    print("--- 2. Nome ao contrário em maiúsculas ---")
    nome = input("Digite seu nome: ").upper()
    print(nome[::-1])

def ex03():
    print("--- 3. Nome na vertical ---")
    nome = input("Digite seu nome: ")
    for letra in nome:
        print(letra)

def ex04():
    print("--- 4. Nome em escada ---")
    nome = input("Digite seu nome: ").upper()
    for i in range(1, len(nome) + 1):
        print(nome[:i])

def ex05():
    print("--- 5. Escada invertida ---")
    nome = input("Digite seu nome: ").upper()
    for i in range(len(nome), 0, -1):
        print(nome[:i])

def ex06():
    print("--- 6. Data por extenso ---")
    meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    data = input("Digite uma data (dd/mm/aaaa): ")
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= mes <= 12:
            print(f"{dia} de {meses[mes]} de {ano}")
        else:
            print("Mês inválido.")
    except:
        print("Formato inválido.")

def ex07():
    print("--- 7. Contar espaços e vogais ---")
    frase = input("Digite uma frase: ").lower()
    espacos = frase.count(' ')
    vogais = sum(frase.count(v) for v in 'aeiouáéíóúãõâêîôû')
    print(f"Espaços: {espacos} | Vogais: {vogais}")

def ex08():
    print("--- 8. Palíndromo ---")
    texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
    # Remove pontuações básicas para testar frases melhor
    texto = ''.join(c for c in texto if c.isalnum())
    if texto == texto[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

def ex09():
    print("--- 9. Verificação de CPF ---")
    cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ").replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return print("Formato inválido. Digite 11 números.")
    
    # Validação real do dígito verificador
    def calcula_digito(cpf_parcial, peso_inicial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calcula_digito(cpf[:9], 10)
    digito2 = calcula_digito(cpf[:9] + digito1, 11)
    
    if cpf[-2:] == digito1 + digito2:
        print("CPF Válido!")
    else:
        print("CPF Inválido!")

def ex10():
    print("--- 10. Número por extenso (até 99) ---")
    unidades = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", 
                "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
    dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    
    try:
        num = int(input("Digite um número até 99: "))
        if 0 <= num < 20:
            print(unidades[num])
        elif 20 <= num <= 99:
            d = num // 10
            u = num % 10
            if u == 0:
                print(dezenas[d])
            else:
                print(f"{dezenas[d]} e {unidades[u].lower()}")
        else:
            print("Número fora do intervalo.")
    except:
        print("Entrada inválida.")

def ex11():
    print("--- 11. Jogo da Forca ---")
    palavras = ["PYTHON", "GITHUB", "PROGRAMACAO", "COMPUTADOR", "DESENVOLVEDOR"]
    palavra = random.choice(palavras)
    letras_certas = ["_"] * len(palavra)
    erros = 0
    max_erros = 6
    
    while erros < max_erros and "_" in letras_certas:
        print("\nPalavra:", " ".join(letras_certas))
        tentativa = input("Digite uma letra: ").upper()
        
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_certas[i] = tentativa
        else:
            erros += 1
            print(f"Você errou! ({erros}/{max_erros})")
            
    if "_" not in letras_certas:
        print(f"\n🎉 Parabéns! A palavra era {palavra}")
    else:
        print(f"\n💀 Fim de jogo. A palavra era {palavra}")

def ex12():
    print("--- 12. Corrigir telefone ---")
    telefone = input("Telefone: ").replace("-", "").strip()
    if len(telefone) == 7:
        print(f"Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        telefone = "3" + telefone
    print(f"Telefone corrigido sem formatação: {telefone}")
    print(f"Telefone corrigido com formatação: {telefone[:4]}-{telefone[4:]}")

def ex13():
    print("--- 13. Palavra embaralhada ---")
    palavras = ["teclado", "mouse", "monitor", "algoritmo"]
    escolhida = random.choice(palavras)
    embaralhada = "".join(random.sample(escolhida, len(escolhida)))
    
    print(f"Adivinhe a palavra: {embaralhada}")
    tentativas = 3
    while tentativas > 0:
        chute = input("Seu palpite: ").lower()
        if chute == escolhida:
            print("Parabéns, você acertou!")
            return
        else:
            tentativas -= 1
            print(f"Errado. Você tem {tentativas} tentativas.")
    print(f"Você perdeu. A palavra era: {escolhida}")

def ex14():
    print("--- 14. Leet Speak ---")
    texto = input("Digite o texto: ").upper()
    substituicoes = {'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    for letra, numero in substituicoes.items():
        texto = texto.replace(letra, numero)
    print(f"Leet Speak: {texto}")

# =======================================================
# MENU PRINCIPAL
# =======================================================
if __name__ == "__main__":
    while True:
        try:
            escolha = int(input("\nDigite o número do exercício para testar (1 a 14) ou 0 para sair: "))
            if escolha == 0:
                print("Encerrando...")
                break
            elif 1 <= escolha <= 14:
                eval(f"ex{escolha:02d}()")
            else:
                print("Por favor, digite um número entre 1 e 14.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")