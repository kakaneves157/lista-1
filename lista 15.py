preco_hora =float(input("digite quanto voce ganha por hora:"))
horas_trabalhadas =float(input('digite quantas horas voce trabalhou esse mes:'))
salario_bruto =preco_hora *horas_trabalhadas
IR = salario_bruto * (11/100)
INSS =salario_bruto * (8/100)
sindicato =salario_bruto *(5/100)
salario_liquido =salario_bruto - IR -ISS - sindicato
print(f"+salario bruto : r$ {salario_bruto:.2f}\n"
      )