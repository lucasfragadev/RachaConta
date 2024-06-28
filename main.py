# Dev. Lucas Fraga - 100 Days of Code: The Complete Python Pro Bootcamp - RachaConta 1.0
# PT-BR: Calculadora que divide o valor total da conta entre pessoas, incluindo gorjetas, para uma divisão justa e precisa.
# EN-US: Calculator that divides the total amount of the bill between people, including tips, for a fair and accurate split.

print("\nBem vindo a calculadora de conta!\n ")

total_conta = input("Qual o valor total da conta? ")
gorjeta = input("Quanto de gorjeta pretende dar? 10, 12 ou 15 (%)? ")
qnt_pessoas = input("Quantas pessoas irão dividir a conta? ")

total_conta_float = float(total_conta)
gorjeta_int = int(gorjeta)
qnt_pessoas_float = float(qnt_pessoas)

total_conta_com_gorjeta = total_conta_float + (total_conta_float * (gorjeta_int / 100))
print(f"O valor total da conta com a porcentagem aplicada é de R$ {total_conta_com_gorjeta:.2f}")

valor_cada = total_conta_com_gorjeta / qnt_pessoas_float
print(f"Por isso, cada pessoa deverá pagar R$ {valor_cada:.2f} ")