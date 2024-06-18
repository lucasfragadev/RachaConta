
# Dev. Lucas Frag - 100 Days of Code: The Complete Python Pro Bootcamp - RachaConta 1.0
# PT-BR: Calculadora que divide o valor total da conta entre pessoas, incluindo gorjetas, para uma divisão justa e precisa.
# EN-US: alculator that divides the total amount of the bill between people, including tips, for a fair and accurate split.

# Mensagem de boas vindas à calculadora! // Welcome to the calculator!
print("\nBem vindo a calculadora de conta!\n ")

# Solicita ao usuário o valor total da conta / Asks the user for the total amount of the bill:
total_conta = input("Qual o valor total da conta? ")

# Em seguida, a porcentagem da gorjeta que o usuário deseja dar / Then the percentage of the tip the user wishes to give:
gorjeta = input("Quanto de gorjeta pretende dar? 10, 12 ou 15 (%)? ")

# Solicitação da quantidade de pessoas que irão dividir a conta / Request the number of people who will share the bill:
qnt_pessoas = input("Quantas pessoas irão dividir a conta? ")

# Conversão das entradas de texto para números / Converting text entries to numbers:
total_conta_float = float(total_conta)
gorjeta_int = int(gorjeta)
qnt_pessoas_float = float(qnt_pessoas)

# Realização do cálculo de valor total da conta com a aplicação da gorjeta /  Calculating the total amount of the bill with the tip applied:
total_conta_com_gorjeta = total_conta_float + (total_conta_float * (gorjeta_int / 100))
#Demonstrativo do valor total com a gorjeta escolhida aplicada:
print(f"O valor total da conta com a porcentagem aplicada é de R$ {total_conta_com_gorjeta:.2f}")

# Calcula o valor que cada pessoa deve pagar / Calculate the amount each person must pay:
valor_cada = total_conta_com_gorjeta / qnt_pessoas_float
print(f"Por isso, cada pessoa deverá pagar R$ {valor_cada:.2f} ")