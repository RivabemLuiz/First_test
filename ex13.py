print("--MENU DO RESTAURANTE--")
print("1-Pizza")
print("2-Hambúrguer")
print("3-Salada")
print("4-Sair")

opcao = 0

while opcao != 4:

    opcao = int(input("Escolha uma opcão: "))

    match opcao:
        case 1:
            print ("Perfeito, vocÊ quer uma pizza")
        case 2:
            print("Perfeito vocÊ quer um hambúrguer")
        case 3:
            print("Perfeito vocÊ quer uma salada")
        case 4: 
            print("Encerrando programa...")
        case _:
            print("Opção inválida")
        