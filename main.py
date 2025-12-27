# Bem-vindo ao seu primeiro programa Python, Cauê!
# Este código faz um mini menu interativo.

print("=== Sistema Nex v1.0 ===")
print("1 - Dizer Olá")
print("2 - Mostrar seu nome")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Olá! Espero que você esteja bem!")
elif opcao == "2":
    print("Seu nome é Cauê, o criador do Nex!")
elif opcao == "3":
    print("Saindo do sistema...")
else:
    print("Opção inválida. Tente novamente!")
