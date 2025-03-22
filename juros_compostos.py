import sympy as sp

# Variáveis
J, Fv, Pv, i, n = sp.symbols('J Fv Pv, i, n')

# Fórmulas Composto
juros = Pv * ((1 + i)**n - 1)
valor_futuro = Pv * (1 + i)**n
valor_presente = Fv / (1 + i)**n

# Formulas Simples
valor_futuro_simples = Pv * (1+(i*n)) 

print("Fórmulas Composto")
print(f"juros: {juros}")
print(f"valor_futuro: {valor_futuro}")
print(f"valor_presente: {valor_presente}")

print("\nFórmulas Simples")
print(f"valor_futuro_simples: {valor_futuro_simples}")

#########################################################################################################
print('\n1) Qual o montante de uma aplicação de R$ 3.000,00 a juros compostos, durante 10 meses, à taxa de 1,4% ao mês?\n')

taxa = sp.Rational(1.4, 100) # 1.4 / 100
periodo = 10 # meses
valor_aplicado = 3000.00

montante = valor_futuro.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
montante = sp.N(montante)
print(f"Montante: {montante:.5f}")
#########################################################################################################
#########################################################################################################
print('\n2) Cecília aplicou R$ 12.000,00 a juros compostos, durante 2 anos, à taxa de 1,5% ao mês. Qual o valor dos juros recebidos?  \n')

taxa = sp.Rational(1.5, 100) # 1.5 / 100
periodo = 24 # meses
valor_aplicado = 12000.00

jr = juros.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
jr = sp.N(jr)
print(f"Juros recebidos: {jr:.5f}")
#########################################################################################################
#########################################################################################################
print('\n3) Qual o capital que deve ser aplicado a juros compostos, à taxa de 1,8% ao mês, durante 8 meses, para dar um montante de R$ 6.000,00?  \n')

taxa = sp.Rational(1.8, 100) # 1.8 / 100
periodo = 8 # meses
montante = 6000.00

va = valor_presente.subs([(Fv, montante), (i, taxa), (n, periodo)])
va = sp.N(va)
print(f"Valor que deve ser aplicado: {va:.5f}")
#########################################################################################################
#########################################################################################################
print(
"""
Um capital de R$ 2.000,00 é aplicado à uma taxa de 3 % ao mês, durante três meses. Os montantes correspondentes obtidos segundo capitalização simples e composta, respectivamente, valem:
    a) R$ 2.180,00 e R$ 2.185,45	b) R$ 2.180,00 e R$ 2.480,00 	
    c) R$ 2.185,45 e R$ 2.480,00 	d) R$ 2.785,45 e R$ 2.480,00      e) R$ 6.180,00 e R$ 4.394,00
"""
)

taxa = sp.Rational(3, 100) # 3 / 100
periodo = 3 # meses
valor_aplicado = 2000.00

mc = valor_futuro.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
mc = sp.N(mc)

ms = valor_futuro_simples.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
ms = sp.N(ms)

print(f"(a) Montante: simples={ms:.5f}, composto={mc:.5f}")
#########################################################################################################
#########################################################################################################
print(
"""
5) Uma empresa tomou um empréstimo bancário de R$ 80.000,00 pelo prazo de 1 ano. Calcule o montante pago sabendo que o banco cobrou juros compostos à taxa de 5% ao trimestre.
"""
)

taxa = sp.Rational(5, 100) # 5 / 100
periodo = 12/3 # meses
valor_aplicado = 80000.00

m = valor_futuro.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
m = sp.N(m)

print(f"Montante pago: {m:.5f}")
#########################################################################################################
#########################################################################################################
print(
"""
6) Uma carteira de investimento rende 2% ao mês a juros compostos. Depois de três meses, R$ 1.500,00 aplicados nessa carteira valem aproximadamente x unidades monetárias. Determine o valor de x.
"""
)

taxa = sp.Rational(2, 100) # 2 / 100
periodo = 3 # meses
valor_aplicado = 1500.00

x = valor_futuro.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
x = sp.N(x)

print(f"Valor de x: {x:.5f}")
#########################################################################################################
#########################################################################################################
print(
"""
7) Afonso pode comprar um terreno por R$ 20.000,00. Ele sabe que o terreno valerá R$ 30.000,00 daqui a 5 anos. Se ele tiver a alternativa de aplicar o dinheiro a juros compostos, à taxa de 9% ao ano, será que a aplicação no terreno valerá a pena?
"""
)

taxa = sp.Rational(9, 100) # 9 / 100
periodo = 5 # meses
valor_aplicado = 20000.00

x = valor_futuro.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
x = sp.N(x)

print(f"Valor total a pagar a com aplicação a juros compostos: {x:.5f}. {'Valeu a pena!' if x < 30000.00 else 'Não valeu a pena!'}")
#########################################################################################################
#########################################################################################################
print(
"""
8) Uma empresa recebeu um cheque no valor de R$ 6.800,00 para ser descontado em 120 dias. 
Necessitando do dinheiro hoje, a empresa solicita ao seu banco o desconto imediato desse cheque. 
Admitindo que o banco irá dar um desconto a uma taxa composta de 1,73% ao mês, quanto que a empresa receberá?
"""
)

taxa = sp.Rational(1.73, 100) # 1.73 / 100
periodo = 4 # meses
valor_aplicado = 6800.00

x = juros.subs([(Pv, valor_aplicado), (i, taxa), (n, periodo)])
x = sp.N(x)

print(f"Empresa receberá: {(valor_aplicado-x):.5f}.")
#########################################################################################################
#########################################################################################################
print(
"""
9) Uma pessoa tem R$ 230.000,00 aplicada em uma poupança que lhe garante uma remuneração de 1,2% ao mês para os próximos 6 meses. 
O gerente do banco entra em contato com o cliente e oferece outras alternativas de investimos que são:
	a) Realizar uma aplicação no valor único de R$ 150.000,00 à uma taxa de 1,65% ao mês, por um prazo de 6 meses;
	b) Realizar uma aplicação no valor único de R$ 230.000,00 a uma taxa de 1,33% ao mês, por um prazo de 6 meses.
Analisando os valores encontrados em cada uma das opções de investimento, informe qual será a melhor alternativa para a pessoa?
"""
)


periodo = 6 # meses
taxa = sp.Rational(1.2, 100)
va = 230000.00

vaf = valor_futuro.subs([(Pv, va), (i, taxa), (n, periodo)])
vaf = sp.N(vaf)

print(f"{vaf:.5f}.")

# a)
a1_taxa = sp.Rational(1.2, 100)
ava1 = 80000.00
a2_taxa = sp.Rational(1.65, 100)
ava2 = 150000.00

a1 = valor_futuro.subs([(Pv, ava1), (i, a1_taxa), (n, periodo)])
a1 = sp.N(a1)

a2 = valor_futuro.subs([(Pv, ava2), (i, a2_taxa), (n, periodo)])
a2 = sp.N(a2)

print(f"a) {a1+a2:.5f}.")

# b)
b_taxa = sp.Rational(1.33, 100)
bva = 230000.00

b = valor_futuro.subs([(Pv, bva), (i, b_taxa), (n, periodo)])
b = sp.N(b)

print(f"b) {b:.5f}.")
#########################################################################################################
#########################################################################################################
print(
"""
10) Determine o valor do investimento inicial que deve ser realizado no regime de juros compostos, 
com uma taxa efetiva de 1,034% ao mês, para produzir um montante acumulado de R$ 35.000,00 no final de 12 meses.  
"""
)

taxa = sp.Rational(1.034, 100) # 1.034 / 100
periodo = 12 # meses
montante_acumulado = 35000.00

va = valor_presente.subs([(Fv, montante_acumulado), (i, taxa), (n, periodo)])
va = sp.N(va)

print(f"Valor Aplicado: {(va):.5f}.")
#########################################################################################################