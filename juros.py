# JUROS SIMPLES
valor_inicial = float(input())
juros = 0.1
meses = 2
valor_juros = valor_inicial * juros
valor_final = 0

for i in range(meses):
    # 720
	valor_final = valor_inicial + valor_juros
	valor_inicial = valor_final

print(valor_inicial)