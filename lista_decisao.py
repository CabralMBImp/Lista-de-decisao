import math
import datetime

# =======================================================
# LISTA DE EXERCÍCIOS - ESTRUTURA DE DECISÃO
# =======================================================

def ex01():
    print("--- Exercício 01 ---")
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    print(f"O maior é: {max(n1, n2)}")

def ex02():
    print("--- Exercício 02 ---")
    n = float(input("Digite um valor: "))
    if n > 0: print("Positivo")
    elif n < 0: print("Negativo")
    else: print("Zero")

def ex03():
    print("--- Exercício 03 ---")
    sexo = input("Digite F ou M: ").strip().upper()
    if sexo == 'F': print("F - Feminino")
    elif sexo == 'M': print("M - Masculino")
    else: print("Sexo Inválido.")

def ex04():
    print("--- Exercício 04 ---")
    letra = input("Digite uma letra: ").strip().lower()
    if len(letra) == 1 and letra.isalpha():
        if letra in 'aeiou': print("Vogal")
        else: print("Consoante")
    else: print("Entrada inválida.")

def ex05():
    print("--- Exercício 05 ---")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media == 10: print("Aprovado com Distinção")
    elif media >= 7: print("Aprovado")
    else: print("Reprovado")

def ex06():
    print("--- Exercício 06 ---")
    n1 = float(input("Num 1: "))
    n2 = float(input("Num 2: "))
    n3 = float(input("Num 3: "))
    print(f"O maior é {max(n1, n2, n3)}")

def ex07():
    print("--- Exercício 07 ---")
    nums = [float(input(f"Num {i+1}: ")) for i in range(3)]
    print(f"Maior: {max(nums)} | Menor: {min(nums)}")

def ex08():
    print("--- Exercício 08 ---")
    p1 = float(input("Preço 1: "))
    p2 = float(input("Preço 2: "))
    p3 = float(input("Preço 3: "))
    menor = min(p1, p2, p3)
    if menor == p1: print("Compre o produto 1")
    elif menor == p2: print("Compre o produto 2")
    else: print("Compre o produto 3")

def ex09():
    print("--- Exercício 09 ---")
    nums = [float(input(f"Num {i+1}: ")) for i in range(3)]
    nums.sort(reverse=True)
    print("Ordem decrescente:", nums)

def ex10():
    print("--- Exercício 10 ---")
    turno = input("Turno (M/V/N): ").strip().upper()
    if turno == 'M': print("Bom Dia!")
    elif turno == 'V': print("Boa Tarde!")
    elif turno == 'N': print("Boa Noite!")
    else: print("Valor Inválido!")

def ex11():
    print("--- Exercício 11 ---")
    salario = float(input("Salário: R$ "))
    if salario <= 280: perc = 20
    elif salario <= 700: perc = 15
    elif salario <= 1500: perc = 10
    else: perc = 5
    aumento = salario * (perc / 100)
    novo = salario + aumento
    print(f"Salário original: R$ {salario:.2f}\nPercentual: {perc}%\nAumento: R$ {aumento:.2f}\nNovo Salário: R$ {novo:.2f}")

def ex12():
    print("--- Exercício 12 ---")
    valor_hora = float(input("Valor da hora: "))
    horas = float(input("Horas trabalhadas: "))
    bruto = valor_hora * horas
    if bruto <= 900: perc_ir = 0
    elif bruto <= 1500: perc_ir = 5
    elif bruto <= 2500: perc_ir = 10
    else: perc_ir = 20
    ir = bruto * (perc_ir / 100)
    inss = bruto * 0.10
    sindicato = bruto * 0.03 # Conforme enunciado
    fgts = bruto * 0.11
    descontos = ir + inss + sindicato
    liquido = bruto - descontos
    print(f"\nSalário Bruto: R$ {bruto:.2f}")
    print(f"(-) IR ({perc_ir}%) : R$ {ir:.2f}")
    print(f"(-) INSS (10%) : R$ {inss:.2f}")
    print(f"(-) Sindicato (3%) : R$ {sindicato:.2f}")
    print(f"FGTS (11%) : R$ {fgts:.2f}")
    print(f"Total de descontos : R$ {descontos:.2f}")
    print(f"Salário Liquido : R$ {liquido:.2f}")

def ex13():
    print("--- Exercício 13 ---")
    dias = {1:"Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
    dia = int(input("Número da semana (1-7): "))
    print(dias.get(dia, "Valor inválido"))

def ex14():
    print("--- Exercício 14 ---")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media >= 9: conceito = 'A'
    elif media >= 7.5: conceito = 'B'
    elif media >= 6: conceito = 'C'
    elif media >= 4: conceito = 'D'
    else: conceito = 'E'
    status = "APROVADO" if conceito in ['A', 'B', 'C'] else "REPROVADO"
    print(f"Notas: {n1}, {n2} | Média: {media:.2f} | Conceito: {conceito} | {status}")

def ex15():
    print("--- Exercício 15 ---")
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))
    l3 = float(input("Lado 3: "))
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        if l1 == l2 == l3: print("Triângulo Equilátero")
        elif l1 == l2 or l1 == l3 or l2 == l3: print("Triângulo Isósceles")
        else: print("Triângulo Escaleno")
    else:
        print("Não formam um triângulo.")

def ex16():
    print("--- Exercício 16 ---")
    a = float(input("Valor de a: "))
    if a == 0:
        print("A equação não é do 2º grau.")
        return
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print("Equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"Equação possui apenas uma raiz real: {raiz}")
    else:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Equação possui duas raízes reais: {r1} e {r2}")

def ex17():
    print("--- Exercício 17 ---")
    ano = int(input("Ano: "))
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    print(f"{ano} {'é' if bissexto else 'não é'} bissexto.")

def ex18():
    print("--- Exercício 18 ---")
    data_str = input("Data (dd/mm/aaaa): ")
    try:
        dia, mes, ano = map(int, data_str.split('/'))
        datetime.date(ano, mes, dia) # O datetime valida automaticamente
        print("Data Válida!")
    except ValueError:
        print("Data Inválida!")

def ex19():
    print("--- Exercício 19 ---")
    num = int(input("Digite um número < 1000: "))
    if num >= 1000 or num < 0:
        print("Número inválido.")
        return
    c = num // 100
    d = (num % 100) // 10
    u = (num % 10)
    partes = []
    if c > 0: partes.append(f"{c} centena{'s' if c > 1 else ''}")
    if d > 0: partes.append(f"{d} dezena{'s' if d > 1 else ''}")
    if u > 0: partes.append(f"{u} unidade{'s' if u > 1 else ''}")
    
    if len(partes) == 3: print(f"{partes[0]}, {partes[1]} e {partes[2]}")
    elif len(partes) == 2: print(f"{partes[0]} e {partes[1]}")
    elif len(partes) == 1: print(partes[0])
    else: print("0 unidades")

def ex20():
    print("--- Exercício 20 ---")
    nums = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    media = sum(nums)/3
    if media == 10: print(f"Aprovado com Distinção. Média {media:.2f}")
    elif media >= 7: print(f"Aprovado. Média {media:.2f}")
    else: print(f"Reprovado. Média {media:.2f}")

def ex21():
    print("--- Exercício 21 ---")
    valor = int(input("Valor do saque (10 a 600): "))
    if valor < 10 or valor > 600:
        print("Valor fora do limite.")
        return
    notas = [100, 50, 10, 5, 1]
    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ {nota}")
            valor -= qtd * nota

def ex22():
    print("--- Exercício 22 ---")
    num = int(input("Número: "))
    print("Par" if num % 2 == 0 else "Ímpar")

def ex23():
    print("--- Exercício 23 ---")
    num = float(input("Número: "))
    print("Inteiro" if num.is_integer() else "Decimal")

def ex24():
    print("--- Exercício 24 ---")
    n1 = float(input("Num 1: "))
    n2 = float(input("Num 2: "))
    op = input("Operação (+, -, *, /): ")
    res = 0
    if op == '+': res = n1 + n2
    elif op == '-': res = n1 - n2
    elif op == '*': res = n1 * n2
    elif op == '/': res = n1 / n2
    else: return print("Operação inválida.")
    
    p_i = "Par" if res % 2 == 0 else "Ímpar"
    p_n = "Positivo" if res > 0 else "Negativo" if res < 0 else "Zero"
    i_d = "Inteiro" if float(res).is_integer() else "Decimal"
    print(f"Resultado: {res} ({p_i}, {p_n}, {i_d})")

def ex25():
    print("--- Exercício 25 ---")
    print("Responda S para Sim ou N para Não:")
    p1 = input("Telefonou para a vítima? ").upper() == 'S'
    p2 = input("Esteve no local do crime? ").upper() == 'S'
    p3 = input("Mora perto da vítima? ").upper() == 'S'
    p4 = input("Devia para a vítima? ").upper() == 'S'
    p5 = input("Já trabalhou com a vítima? ").upper() == 'S'
    
    sims = sum([p1, p2, p3, p4, p5])
    if sims == 2: print("Suspeita")
    elif 3 <= sims <= 4: print("Cúmplice")
    elif sims == 5: print("Assassino")
    else: print("Inocente")

def ex26():
    print("--- Exercício 26 ---")
    litros = float(input("Litros: "))
    tipo = input("Tipo (A-álcool, G-gasolina): ").upper()
    
    if tipo == 'A':
        preco = 1.90
        desc = 0.03 if litros <= 20 else 0.05
    elif tipo == 'G':
        preco = 2.50
        desc = 0.04 if litros <= 20 else 0.06
    else:
        return print("Tipo inválido.")
        
    total = (preco * litros) * (1 - desc)
    print(f"Valor a pagar: R$ {total:.2f}")

def ex27():
    print("--- Exercício 27 ---")
    kg_morango = float(input("Kg de Morango: "))
    kg_maca = float(input("Kg de Maçã: "))
    
    p_morango = 2.50 if kg_morango <= 5 else 2.20
    p_maca = 1.80 if kg_maca <= 5 else 1.50
    
    total = (kg_morango * p_morango) + (kg_maca * p_maca)
    kg_total = kg_morango + kg_maca
    
    if kg_total > 8 or total > 25:
        total *= 0.90 # Desconto de 10%
        
    print(f"Valor a pagar: R$ {total:.2f}")

def ex28():
    print("--- Exercício 28 ---")
    print("Tipos de carne: 1- File Duplo | 2- Alcatra | 3- Picanha")
    tipo = int(input("Escolha o tipo: "))
    kg = float(input("Quantidade (Kg): "))
    cartao = input("Cartão Tabajara? (S/N): ").upper() == 'S'
    
    if tipo == 1:
        nome = "File Duplo"
        preco = 4.90 if kg <= 5 else 5.80
    elif tipo == 2:
        nome = "Alcatra"
        preco = 5.90 if kg <= 5 else 6.80
    elif tipo == 3:
        nome = "Picanha"
        preco = 6.90 if kg <= 5 else 7.80
    else:
        return print("Carne inválida.")
        
    total = kg * preco
    desconto = total * 0.05 if cartao else 0
    pagar = total - desconto
    
    print("\n--- CUPOM FISCAL ---")
    print(f"Carne: {nome}")
    print(f"Quantidade: {kg} Kg")
    print(f"Preço Total: R$ {total:.2f}")
    print(f"Tipo Pagamento: {'Cartão Tabajara' if cartao else 'Outro'}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor a Pagar: R$ {pagar:.2f}")

# =======================================================
# MENU PARA EXECUTAR OS EXERCÍCIOS
# =======================================================
if __name__ == "__main__":
    while True:
        try:
            escolha = int(input("\nDigite o número do exercício para testar (1 a 28) ou 0 para sair: "))
            if escolha == 0:
                print("Encerrando...")
                break
            elif 1 <= escolha <= 28:
                # Chama a função baseada no número digitado usando eval (ex: ex01(), ex15())
                eval(f"ex{escolha:02d}()")
            else:
                print("Por favor, digite um número entre 1 e 28.")
        except Exception as e:
            print(f"Ocorreu um erro na execução: {e}")