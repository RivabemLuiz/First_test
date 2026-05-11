print("CONVERSOR DE UNIDADES")
print("1-Metros para milímetros")
print("2-Metros para centímetros")
print("3-Metros para quilometros")
print("4-Sair")

opcao = 0

while opcao != 4:
    opcao = int(input("Para qual unidade você quer converter? "))

    match opcao:
        case 1:
            metros = float(input("Digite sua medida em metros: "))
            mm = metros * 1000
            print(f"Para {metros:.2f} m você tem {mm:.2f} mm")
        case 2:
            metros = float(input("Digite sua medida em metros: "))
            cm = metros * 100
            print(f"Para {metros:.2f} m você tem {cm:.2f} cm")
        case 3:
            metros = float(input("Digite sua medida em metros: "))
            km = metros / 1000
            print(f"Para {metros:.2f} m você tem {km:.2f} km")
        case 4: 
            print("Encerrando programa...")
        case _:
            print("Opção inválida.")    
 

