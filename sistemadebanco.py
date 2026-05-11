opcoes = ["SAIR","SACAR","DEPOSITAR"]
print("--SISTEMA DE BANCO--")

saldo = float(input("Qual seu saldo? "))


while True: 
    print("1-Sacar")
    print("2-Depositar")
    print("0-Sair")
    
    opcao = float(input("Escolha uma opcão: "))
    
    match opcao:
        case 1:
            valor = float(input("Qual o valor? "))

            if valor <= saldo:
                saldo -= valor
                print (f"Saque realizado, seu saldo agora é: {saldo:.2f}")
            else:
                print("Saldo insuficiente.")

        case 2:
            valor = float(input("Qual o valor? "))
            saldo += valor
            print(f"OK, seu saldo agora é: {saldo:.2f}")

        case 0:
            print("Encerrando programa")
            break

        case _:
            print("Opção inválida")

    
    





