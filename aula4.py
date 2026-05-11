MAX_TENTATIVAS = 3
tentativas = 0
senha = input("Digite a senha: ")

is_valid = (senha == "1234")
while not is_valid and tentativas < MAX_TENTATIVAS:
    print("Senha incorreta!")
    senha = input("Digite sua senha: ")
    
    is_valid = (senha == "1234")
    tentativas += 1

if (is_valid):
    print("Entrada permitida")
else:
    print("Acesso NEGADO")