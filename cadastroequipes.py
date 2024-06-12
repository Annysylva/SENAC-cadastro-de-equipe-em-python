def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    email = input("Digite o email do aluno: ")
    
    aluno = f"Nome: {nome}, Idade: {idade}, Email: {email}\n"
    
    with open("equipe.txt", "a") as arquivo:
        arquivo.write(aluno)
    
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    try:
        with open("equipe.txt", "r") as arquivo:
            print("Lista de Alunos:")
            print(arquivo.read())
    except FileNotFoundError:
        print("Ainda não há alunos cadastrados.")

def menu():
    while True:
        print("\n==== Menu ====")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            listar_alunos()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
