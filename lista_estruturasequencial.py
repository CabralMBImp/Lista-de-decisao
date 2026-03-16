import math

# =======================================================
# LISTA DE EXERCÍCIOS - ESTRUTURA SEQUENCIAL
# =======================================================

def ex01():
    print("--- 1. Mensagem ---")
    print("Alô mundo")

def ex02():
    print("--- 2. Mostrar Número ---")
    numero = input("Digite um número: ")
    print(f"O número informado foi {numero}.")

def ex03():
    print("--- 3. Soma ---")
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    print(f"A soma é: {n1 + n2}")

def ex04():
    print("--- 4. Média Bimestral ---")
    notas = [float(input(f"Digite a nota do {i}º bimestre: ")) for i in range(1, 5)]
    print(f"A média é: {sum(notas) / 4:.2f}")

def ex05():
    print("--- 5. Metros para Centímetros ---")
    metros = float(input("Digite o valor em metros: "))
    print(f"{metros}m equivale a {metros * 100}cm.")

def ex06():
    print("--- 6. Área do Círculo ---")
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f}")

def ex07():
    print("--- 7. Área do Quadrado ---")
    lado = float(input("Digite o lado do quadrado: "))
    area = lado ** 2
    print(f"A área é {area} e o dobro da área é {area * 2}")

def ex08():
    print("--- 8. Salário Mensal ---")
    valor_hora = float(input("Quanto você ganha por hora? R$ "))
    horas = float(input("Quantas horas trabalhou no mês? "))
    print(f"Seu salário total neste mês é: R$ {valor_hora * horas:.2f}")

def ex09():
    print("--- 9. Fahrenheit para Celsius ---")
    f = float(input("Temperatura em Fahrenheit: "))
    c = 5 * ((f - 32) / 9)
    print(f"A temperatura em Celsius é: {c:.2f}°C")

def ex10():
    print("--- 10. Celsius para Fahrenheit ---")
    c = float(input("Temperatura em Celsius: "))
    f = (c * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {f:.2f}°F")

def ex11():
    print("--- 11. Operações com 3 números ---")
    i1 = int(input("Digite o 1º número inteiro: "))
    i2 = int(input("Digite o 2º número inteiro: "))
    r1 = float(input("Digite um número real: "))
    
    a = (i1 * 2) * (i2 / 2)
    b = (i1 * 3) + r1
    c = r1 ** 3
    
    print(f"a) Produto do dobro do primeiro com metade do segundo: {a}")
    print(f"b) Soma do triplo do primeiro com o terceiro: {b}")
    print(f"c) Terceiro elevado ao cubo: {c:.2f}")

def ex12():
    print("--- 12. GB para MB ---")
    gb = float(input("Valor em Gigabytes (GB): "))
    print(f"{gb} GB = {gb * 1024} MB")

def ex13():
    print("--- 13. GB para MB e KB ---")
    gb = float(input("Valor em Gigabytes (GB): "))
    mb = gb * 1024
    kb = mb * 1024
    print(f"{gb} GB = {mb} MB = {kb} KB")

def ex14():
    print("--- 14. João Papo-de-Pescador ---")
    peso = float(input("Qual o peso dos peixes pescados (kg)? "))
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print(f"Houve um excesso de {excesso:.2f} kg.")
        print(f"João deverá pagar uma multa de R$ {multa:.2f}.")
    else:
        print("Peso dentro do limite (50kg). Não há multa a pagar.")

def ex15():
    print("--- 15. Salário com Descontos ---")
    valor_hora = float(input("Quanto você ganha por hora? R$ "))
    horas = float(input("Quantas horas trabalhou no mês? "))
    
    bruto = valor_hora * horas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato
    
    print(f"+ Salário Bruto : R$ {bruto:.2f}")
    print(f"- IR (11%) : R$ {ir:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}")
    print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
    print(f"= Salário Líquido : R$ {liquido:.2f}")

def ex16():
    print("--- 16. Loja de Tintas (Simples) ---")
    area = float(input("Tamanho da área a ser pintada (m²): "))
    litros_necessarios = area / 3
    latas = math.ceil(litros_necessarios / 18)
    preco = latas * 80
    
    print(f"Você precisará de {latas} lata(s) de 18L.")
    print(f"Preço total: R$ {preco:.2f}")

def ex17():
    print("--- 17. Loja de Tintas (Avançado) ---")
    area = float(input("Tamanho da área a ser pintada (m²): "))
    area_com_folga = area * 1.1
    litros = area_com_folga / 6
    
    latas_sozinhas = math.ceil(litros / 18)
    preco_latas = latas_sozinhas * 80
    
    galoes_sozinhos = math.ceil(litros / 3.6)
    preco_galoes = galoes_sozinhos * 25
    
    latas_mix = int(litros // 18)
    litros_restantes = litros % 18
    galoes_mix = math.ceil(litros_restantes / 3.6)
    preco_mix = (latas_mix * 80) + (galoes_mix * 25)
    
    print("\n--- Resultados (já com 10% de folga) ---")
    print(f"Opção 1 (Apenas Latas): {latas_sozinhas} lata(s) -> R$ {preco_latas:.2f}")
    print(f"Opção 2 (Apenas Galões): {galoes_sozinhos} galão(ões) -> R$ {preco_galoes:.2f}")
    print(f"Opção 3 (Mistura Otimizada): {latas_mix} lata(s) e {galoes_mix} galão(ões) -> R$ {preco_mix:.2f}")

def ex18():
    print("--- 18. Tempo de Download ---")
    tamanho_mb = float(input("Tamanho do arquivo (MB): "))
    velocidade_mbps = float(input("Velocidade da Internet (Mbps): "))
    
    velocidade_mbs = velocidade_mbps / 8
    tempo_segundos = tamanho_mb / velocidade_mbs
    tempo_minutos = tempo_segundos / 60
    
    print(f"O tempo aproximado de download será de {tempo_minutos:.2f} minutos.")

# =======================================================
# MENU PRINCIPAL (Totalmente Revisado)
# =======================================================
if __name__ == "__main__":
    while True:
        try:
            escolha = int(input("\nQual exercício testar? (1 a 18) ou 0 para sair: "))
            if escolha == 0:
                print("Encerrando...")
                break
            elif 1 <= escolha <= 18:
                eval(f"ex{escolha:02d}()")
            else:
                print("Por favor, digite um número entre 1 e 18.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")