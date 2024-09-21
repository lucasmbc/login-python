usuario_correto = "admin"
senha_correta = "1234"

def sistema_login():
    tentativas = 3
    
    while tentativas > 0:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        if usuario == usuario_correto and senha == senha_correta:
            print(f"\nBem-vindo, {usuario}!")
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Credenciais incorretas. Você tem {tentativas} tentativas restantes.\n")
            else:
                print("\nVocê usou todas as suas tentativas.")
    
    for _ in range(3):
        print("Acesso bloqueado.")

sistema_login()
